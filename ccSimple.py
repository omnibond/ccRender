import bpy
import time
import threading
import random
import re
from bpy.app.handlers import persistent
from urllib.parse import urlparse

import paramiko
from scp import SCPClient

bl_info = {
    "name": "CC Render",
    "author": "Omnibond",
    "version": (0, 4),
    "blender": (2, 77, 0),
    "location": "View3D > Tools > ccSimple_Render",
    "description": "Cloudy Cluster Simple Render (alpha stage)",
    "warning": "",
    "wiki_url": "",
    "category": "ccRender"}


class Communicator():
    def __init__(self):
        self._schedulerURI = None
        self._username = None
        self._password = None
        self._numNodes = 0
        self._blendPath = None
        self._progressText = "initializing..."
        self._progress = True
        self._finished = False
        self._sshClient = paramiko.SSHClient()
        self._scpClient = None

    @property
    def schedulerURI(self):
        return self._schedulerURI

    @schedulerURI.setter
    def schedulerURI(self, value):
        self._schedulerURI = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def numNodes(self):
        return self._numNodes

    @numNodes.setter
    def numNodes(self, value):
        self._numNodes = value

    @property
    def blendPath(self):
        return self._blendPath

    @blendPath.setter
    def blendPath(self, value):
        self._blendPath = value

    @property
    def progressText(self):
        return self._progressText

    @progressText.setter
    def progressText(self, value):
        self._progress = True
        print(value)
        self._progressText = value

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value

    @property
    def sshClient(self):
        return self._sshClient

    @sshClient.setter
    def sshClient(self, value):
        self._sshClient = value

    @property
    def scpClient(self):
        return self._scpClient

    @scpClient.setter
    def scpClient(self, value):
        self._scpClient = value

    def render(self):
        self.progressText = "Connecting to scheduler..."
        result = self.connect()
        if(result is False):
            self.finished = True
            return False

        self.progressText = "done."

        self.progressText = "scp'ing blend file..."
        result = self.sendBlend()
        if(result is False):
            self.finished = True
            return False
        self.progressText = "done."
        self.finished = True

    def connect(self):

        self.sshClient.load_system_host_keys()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.sshClient.connect(self.schedulerURI, 22, self.username, self.password)

            self.scpClient = SCPClient(self.sshClient.get_transport())

        except BadHostKeyException as err:
            self.progressText = "SSH Connection failed: Bad host key."
            return False
        except AuthenticationException as err:
            self.progressText = "SSH Connection failed: Authentication Error."
            return False
        except SSHException as err:
            self.progressText = "SSH Connection failed: " + err
            return False
        except socket.error as err:
            self.progressText = "SSH Connection failed: " + err
            return False

        return True

    def sendBlend(self):
        time.sleep(2)
        return True

    def disconnect(self):
        if self.sshClient is not None:
            self.sshClient.close()
            self.sshClient = None

communicator = Communicator()


class ccModalTimerOperator(bpy.types.Operator):
    # Operator which runs its self from a ccModalTimerOperator
    bl_idname = "wm.ccmodal_timer_opt"
    bl_label = "ccModal Timer Operator"
    anyKeyEventTypes = {'LEFTMOUSE', 'RIGHTMOUSE', 'ESC', 'SPACE', 'OSKEY',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                        'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE',
                        'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE',
                        'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT',
                        'RIGHT_CTRL', 'RIGHT_SHIFT', 'GRLESS', 'TAB', 'RET',
                        'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON',
                        'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS',
                        'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET',
                        'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW',
                        'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4',
                        'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3',
                        'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD',
                        'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0',
                        'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1',
                        'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
                        'F11', 'F12', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP',
                        'PAGE_DOWN', 'END'}

    def isAnyKey(self, event):
        return event.type in self.anyKeyEventTypes

    def modal(self, context, event):
        if self.isAnyKey(event) is True:
            self.cancel(context)
            return {'FINISHED'}

        if communicator.finished is True:
            # finished ok.
            print ("finished is true.")
            self.cancel(context)
            return {'FINISHED'}

        if communicator.progress is True:
            message = communicator.progressText
            communicator.progress = False
            context.area.header_text_set(message)

        return {'PASS_THROUGH'}

    def validateUpdateInputs(self, context):
        ccSchedulerURI = context.scene.ccSchedulerURI
        ccUsername = context.scene.ccUsername
        ccPassword = context.scene.ccPassword
        ccNumNodes = context.scene.ccNumNodes

        # TODO: valudate the variables here
        # if anything goes wrong return False

        ccSchCheck = urlparse(ccSchedulerURI)
        ccURegex = re.fullmatch(r"^[a-z_][a-z0-9_-]*[$]?$", ccUsername)
        ccPRegex = re.fullmatch(r"^[A-Za-z0-9_]+$", ccPassword)

        if ccSchCheck.path == '':
            ccvalidateMsg = "Invalid URL, it needs an IPv4 or Domain Name"
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        # Username follows basic gnu/linux name rules
        if ccURegex is None:
            ccvalidateMsg = ("Invalid Username. Username must be in letters, "
                             "numbers, '_', '-', or '$'!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        if len(ccUsername) > 32:
            ccvalidateMsg = ("Username is too long, "
                             "it must be less than 32 characters!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        # Password follows the same rules as username
        if ccPRegex is None:
            ccvalidateMsg = ("Invalid Password! Password must be in letters, "
                             "numbers, '_', '-', or '$'!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        if len(ccPassword) > 32:
            ccvalidateMsg = ("Your password is too long, "
                             "it must be less than 32 character!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        # write valid inputs into the communicator
        communicator.schedulerURI = ccSchedulerURI
        communicator.username = ccUsername
        communicator.password = ccPassword
        communicator.numNodes = ccNumNodes

        return True

    def execute(self, context):
        wm = context.window_manager
        self._count = 0
        self._timer = wm.event_timer_add(0.1, context.window)
        wm.modal_handler_add(self)
        communicator.finished = False

        result = self.validateUpdateInputs(context)

        if result is True:
            render()
        else:
            communicator.progressText = result

        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        context.area.header_text_set()
        wm.event_timer_remove(self._timer)
        return {'CANCELLED'}


class ccRenderPanel(bpy.types.Panel):
    '''Creates the ccRender Panel'''
    bl_label = 'ccRender Settings'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'ccSimple_Render'

    # input variables
    # store them on the scene so they can be accessed elsewhere
    bpy.types.Scene.ccSchedulerURI = bpy.props.StringProperty(
        name="CC Scheduler URI"
    )
    bpy.types.Scene.ccUsername = bpy.props.StringProperty(
        name="CC Username"
    )
    bpy.types.Scene.ccPassword = bpy.props.StringProperty(
        name="CC Password",
        subtype='PASSWORD'
    )
    bpy.types.Scene.ccNumNodes = bpy.props.IntProperty(
        name="Number of render nodes",
        default=4,
        min=1,
        max=1000,
        step=1
    )

    def check(self, context):
        return communicator.progress

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Custom Interface!")

        row = col.row()
        row.prop(context.scene, "ccSchedulerURI")
        row = col.row()
        row.prop(context.scene, "ccUsername")
        row = col.row()
        row.prop(context.scene, "ccPassword")
        row = col.row()
        row.prop(context.scene, "ccNumNodes")

        col = layout.column()
        row = col.row()

        # Test Button. Will display "Progress" bar on header instead of panel
        # will leave upon Esc or Right Mouse button.
        row.operator(operator="wm.ccmodal_timer_opt", text="Begin Render")


class KickoffRender(threading.Thread):
    def __init__(self, communicator, *args, **kwargs):
        super(KickoffRender, self).__init__(*args, **kwargs)
        self.communicator = communicator

    def run(self):
        self.communicator.render()


def render():
    # communicator.blendPath = bpy.data.filepath
    # bpy.ops.file.pack_all()

    # this doesn't hang, and prints while it works
    # not sure how to report progress

    rdr = KickoffRender(communicator=communicator)
    rdr.start()

    # non-threaded version
    # this hangs while it completed
    # communicator.render()


def register():
    bpy.utils.register_class(ccRenderPanel)
    bpy.utils.register_class(ccModalTimerOperator)


def unregister():
    bpy.utils.unregister_class(ccRenderPanel)
    bpy.utils.unregister_class(ccModalTimerOperator)
