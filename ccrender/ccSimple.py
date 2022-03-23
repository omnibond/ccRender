import bpy
import errno
import os
import re
import socket
import time
import threading
import decimal

import pyperclip


from urllib.parse import urlparse
from threading import Lock

import paramiko
from scp import SCPClient

bl_info = {
    "name": "CC Render",
    "author": "Omnibond",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Tools (Sidebar) > ccSimple_Render",
    "description": "Cloudy Cluster Simple Render",
    "warning": "",
    "wiki_url": "",
    "category": "ccRender"}


class Communicator():

    def __init__(self):
        self._schedulerURI = None
        self._webDavURI = None
        self._vidDavURI = None
        self._imgDavURI = None
        self._username = None
        self._password = None
        self._shareName = None
        self._schedulerType = None
        self._numNodes = 0
        self._spotPrice = False
        self._spAmount = 0.00
        self._instanceType = None
        self._videoOption = False
        self._videoType = None
        self._frameIdx = 0
        self._frameTOT = 0
        self._numPluses = 0
        self._plusCnt = 0
        self._ccIndex = 0
        self._nodeIdx = 0
        self._rDone = 0
        self._ccFRMStart = None
        self._ccFRMEnd = None
        self._blendPath = None
        self._blendName = None
        self._blendDone = None
        self._destPath = None
        self._destName = None
        self._rendDest = None
        self._vidDest = None
        self._blendVid = None
        self._imgSeq = None
        self._ccqBlender = None
        self._blenderJS = None
        self._progressText = "initializing..."
        self._progress = True
        self._finished = False
        self._rProgress = False
        self._sshClient = paramiko.SSHClient()
        self._sftpClient = None
        self._scpClient = None
        self._sshOutput = ""
        self._sshStdout = None

    @property
    def schedulerURI(self):
        return self._schedulerURI

    @schedulerURI.setter
    def schedulerURI(self, value):
        self._schedulerURI = value

    @property
    def webDavURI(self):
        return self._webDavURI

    @webDavURI.setter
    def webDavURI(self, value):
        self._webDavURI = value

    @property
    def vidDavURI(self):
        return self._vidDavURI

    @vidDavURI.setter
    def vidDavURI(self, value):
        self._vidDavURI = value

    @property
    def imgDavURI(self):
        return self._imgDavURI

    @imgDavURI.setter
    def imgDavURI(self, value):
        self._imgDavURI = value

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
    def shareName(self):
        return self._shareName

    @shareName.setter
    def shareName(self, value):
        self._shareName = value

    @property
    def schedulerType(self):
        return self._schedulerType

    @schedulerType.setter
    def schedulerType(self, value):
        self._schedulerType = value

    @property
    def numNodes(self):
        return self._numNodes

    @numNodes.setter
    def numNodes(self, value):
        self._numNodes = value

    @property
    def spotPrice(self):
        return self._spotPrice

    @spotPrice.setter
    def spotPrice(self, value):
        self._spotPrice = value

    @property
    def spAmount(self):
        return self._spAmount

    @spAmount.setter
    def spAmount(self, value):
        self._spAmount = value

    @property
    def instanceType(self):
        return self._instanceType

    @instanceType.setter
    def instanceType(self, value):
        self._instanceType = value

    @property
    def videoOption(self):
        return self._videoOption

    @videoOption.setter
    def videoOption(self, value):
        self._videoOption = value

    @property
    def videoType(self):
        return self._videoType

    @videoType.setter
    def videoType(self, value):
        self._videoType = value

    @property
    def frameIdx(self):
        return self._frameIdx

    @frameIdx.setter
    def frameIdx(self, value):
        self._frameIdx = value

    @property
    def frameTOT(self):
        return self._frameTOT

    @frameTOT.setter
    def frameTOT(self, value):
        self._frameTOT = value

    @property
    def numPluses(self):
        return self._numPluses

    @numPluses.setter
    def numPluses(self, value):
        self._numPluses = value

    @property
    def plusCnt(self):
        return self._plusCnt

    @plusCnt.setter
    def plusCnt(self, value):
        self._plusCnt = value

    @property
    def ccIndex(self):
        return self._ccIndex

    @ccIndex.setter
    def ccIndex(self, value):
        self._ccIndex = value

    @property
    def nodeIdx(self):
        return self._nodeIdx

    @nodeIdx.setter
    def nodeIdx(self, value):
        self._nodeIdx = value

    @property
    def rDone(self):
        return self._rDone

    @rDone.setter
    def rDone(self, value):
        self._rDone = value

    @property
    def ccFRMStart(self):
        return self._ccFRMStart

    @ccFRMStart.setter
    def ccFRMStart(self, value):
        self._ccFRMStart = value

    @property
    def ccFRMEnd(self):
        return self._ccFRMEnd

    @ccFRMEnd.setter
    def ccFRMEnd(self, value):
        self._ccFRMEnd = value

    @property
    def blendPath(self):
        return self._blendPath

    @blendPath.setter
    def blendPath(self, value):
        self._blendPath = value

    @property
    def blendName(self):
        return self._blendName

    @blendName.setter
    def blendName(self, value):
        self._blendName = value

    @property
    def destPath(self):
        return self._destPath

    @destPath.setter
    def destPath(self, value):
        self._destPath = value

    @property
    def blendDone(self):
        return self._blendDone

    @blendDone.setter
    def blendDone(self, value):
        self._blendDone = value

    @property
    def destName(self):
        return self._destName

    @destName.setter
    def destName(self, value):
        self._destName = value

    @property
    def rendDest(self):
        return self._rendDest

    @rendDest.setter
    def rendDest(self, value):
        self._rendDest = value

    @property
    def vidDest(self):
        return self._vidDest

    @vidDest.setter
    def vidDest(self, value):
        self._vidDest = value

    @property
    def blendVid(self):
        return self._blendVid

    @blendVid.setter
    def blendVid(self, value):
        self._blendVid = value

    @property
    def imgSeq(self):
        return self._imgSeq

    @imgSeq.setter
    def imgSeq(self, value):
        self._imgSeq = value

    @property
    def ccqBlender(self):
        return self._ccqBlender

    @ccqBlender.setter
    def ccqBlender(self, value):
        self._ccqBlender = value

    @property
    def blenderJS(self):
        return self._blenderJS

    @blenderJS.setter
    def blenderJS(self, value):
        self._blenderJS = value

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
    def rProgress(self):
        return self._rProgress

    @rProgress.setter
    def rProgress(self, value):
        self._rProgress = value

    @property
    def sshClient(self):
        return self._sshClient

    @sshClient.setter
    def sshClient(self, value):
        self._sshClient = value

    @property
    def sftpClient(self):
        return self._sftpClient

    @sftpClient.setter
    def sftpClient(self, value):
        self._sftpClient = value

    @property
    def scpClient(self):
        return self._scpClient

    @scpClient.setter
    def scpClient(self, value):
        self._scpClient = value

    @property
    def sshOutput(self):
        return self._sshOutput

    @sshOutput.setter
    def sshOutput(self, value):
        self._sshOutput = value

    @property
    def sshStdout(self):
        return self._sshStdout

    @sshStdout.setter
    def sshStdout(self, value):
        self._sshStdout = value

    def render(self):
        result = self.connect()
        if(result is False):
            self.finished = True
            return False

        self.progressText = "done."

        self.progressText = "scp'ing blend file & job script..."
        prepResult = self.blendPrep()
        if(prepResult is False):
            self.finished = True
            return False

        if(self.schedulerType == "TORQUE"):
            prepCCQResult = self.ccqTSetup()
        else:
            prepCCQResult = self.ccqSSetup()
        if(prepCCQResult is False):
            self.finished = True
            return False

        sendResult = self.sendBlend()
        if(sendResult is False):
            self.finished = True
            return False

        self.progressText = "Rendering blend file...."
        rendResult = self.blendRender()
        if(rendResult is False):
            self.finished = True
            return False

        self.progressText = "Creating Resourses...."
        blendprog = self.progressRender()
        if(blendprog is False):
            self.finished = True
            return False

        self.progressText = "Rendering complete!"

        if(self.videoOption is True):
            self.progressText = "Converting frame images into video..."
            videoprog = self.ImageSequence()
            if(videoprog is False):
                self.finished = True
                return False

        self.progressText = "Convertion complete!"

        self.disconnect()

        self.finished = True

    def connect(self):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshClient.load_system_host_keys()

        try:
            self.progressText = 'Connecting to scheduler...'

            self.sshClient.connect(
                self.schedulerURI, 22, self.username, self.password
            )
            self.progressText = 'ssh connection established.'

        except paramiko.BadHostKeyException as err:
            self.progressText = 'SSH Connection failed: Bad Host Key.'
            return False
        except paramiko.AuthenticationException as err:
            self.progressText = 'SSH Connection failed: Authentication Error'
            return False
        except paramiko.SSHException as err:
            self.progressText = 'SSH Connection failed: ' + err
            return False
        except socket.error as err:
            self.progressText = 'SSH Connection failed: ' + err
            return False

        return True

    def blendPrep(self):
        self.blendPath = os.path.dirname(bpy.data.filepath)
        self.blendName = bpy.path.basename(bpy.data.filepath)
        self.destPath = '/mnt/' + self.shareName + '/'
        self.destName = bpy.path.display_name_from_filepath(bpy.data.filepath)

        self.blendDest = self.destPath + self.destName + '/'
        self.rendDest = self.blendDest + 'frames/'
        self.vidDest = self.blendDest + 'video/'
        self.rBlend = self.blendDest + self.blendName
        self.imgDavURI = "https://" + self.schedulerURI + self.rendDest
        self.vidDavURI = "https://" + self.schedulerURI + self.vidDest

        # Set-up the WebDav link based on if the user's reponse
        # for video option.

        if(self.videoOption is True):
            self.webDavURI = self.vidDavURI
        else:
            self.webDavURI = self.imgDavURI

        time.sleep(2)

        # Checks the path of the blend file and tells the user to save
        # the blend file first. This only happens when user is making from
        # brand new blend file.

        if not self.blendPath:
            print("Error: Save file first")
            self.progressText = 'Error: Save file first!'
            return False

        # Changes overwrite to false and saves blend file before sending.
        bpy.context.scene.render.use_overwrite = False
        bpy.ops.wm.save_mainfile()

        return True

    def ccqSSetup(self):
            # Template script for Slurm HPC Scheduler to be added to the cluster.
            # Local placeholder for blender job script.

            self.blenderJS = self.blendPath + "/blender.sh"
            self.ccqBlender = self.blendDest + 'blender.sh'

            # Converts float into a decimal.
            # Round to two decimal places.

            d = decimal.Decimal(self.spAmount)

            spDecimal = d.quantize(decimal.Decimal(10) ** -2)

            if(self.spotPrice is True):
                slurmTemp = (
                    "#!/bin/bash\n\n"

                    "#CC -us yes\n"
                    "#CC -sp {spSTarget}\n"
                    "#CC -it {sInstance}\n\n"

                    "#Slurm HPC Scheduler\n\n"

                    "#SBATCH -N {sNodes}\n\n"

                    "#Shared FS is the same name specified in the CloudyCluster\n"
                    "#creation wizard when launching the cluster.\n"
                    "export SHARED_FS_NAME=/mnt/{sFSNAME} \n\n"

                    "#Blender version for Scheduler\n"
                    "module add blender/2.76\n\n"

                    "cd $SHARED_FS_NAME/blender/2.76\n"
                    "mpiexec blender -b $SHARED_FS_NAME/{sBlendDIR}/{sBlendFile} -o "
                    "$SHARED_FS_NAME'/{sBlendDIR}/frames/frame_#' -E CYCLES -F PNG -a &&\n"
                    "mpirun printf '+' >> $SHARED_FS_NAME/{sBlendDIR}/blendDone.txt\n"
                )

                slurmContext = {
                    "spSTarget": str(spDecimal),
                    "sInstance": self.instanceType,
                    "sNodes": self.numNodes,
                    "sFSNAME": self.shareName,
                    "sBlendDIR": self.destName,
                    "sBlendFile": self.blendName
                }

            else:
                slurmTemp = (
                    "#!/bin/bash\n\n"

                    "#Slurm HPC Scheduler\n\n"

                    "#SBATCH -N {sNodes}\n\n"

                    "#Shared FS is the same name specified in the CloudyCluster\n"
                    "#creation wizard when launching the cluster.\n"
                    "export SHARED_FS_NAME=/mnt/{sFSNAME} \n\n"

                    "#Blender version for Scheduler\n"
                    "module add blender/2.76\n\n"

                    "cd $SHARED_FS_NAME/blender/2.76\n"
                    "mpiexec blender -b $SHARED_FS_NAME/{sBlendDIR}/{sBlendFile} -o "
                    "$SHARED_FS_NAME'/{sBlendDIR}/frames/frame_#' -E CYCLES -F PNG -a &&\n"
                    "mpirun printf '+' >> $SHARED_FS_NAME/{sBlendDIR}/blendDone.txt\n"
                )

                slurmContext = {
                    "sNodes": self.numNodes,
                    "sFSNAME": self.shareName,
                    "sBlendDIR": self.destName,
                    "sBlendFile": self.blendName
                }

            # "newline='\n' " is needed for Windows users to make a job script
            # the same way as for Unix users.

            with open(self.blenderJS, 'w', newline="\n") as blendSlurm:
                blendSlurm.write(slurmTemp.format(**slurmContext))

            return True

    def ccqTSetup(self):
            # Template script for Torque/Maui HPC Scheduler to be added to the cluster.
            # Local placeholder for blender job script.

            self.blenderJS = self.blendPath + "/blender.sh"
            self.ccqBlender = self.blendDest + 'blender.sh'

            # Converts float into a decimal.
            # Round to two decimal places.

            d = decimal.Decimal(self.spAmount)

            spDecimal = d.quantize(decimal.Decimal(10) ** -2)

            if(self.spotPrice is True):
                torqueTemp = (
                    "#!/bin/bash\n\n"

                    "#CC -us yes\n"
                    "#CC -sp {spTTarget}\n"
                    "#CC -it {tInstance}\n\n"

                    "#Torque/Maui HPC Scheduler\n\n"

                    "#PBS -l nodes={tNodes}\n\n"

                    "#Shared FS is the same name specified in the CloudyCluster\n"
                    "#creation wizard when launching the cluster.\n"
                    "export SHARED_FS_NAME=/mnt/{tFSNAME} \n\n"

                    "#Blender version for Scheduler\n"
                    "module add blender/2.76\n\n"

                    "cd $SHARED_FS_NAME/blender/2.76\n"
                    "mpiexec blender -b $SHARED_FS_NAME/{tBlendDIR}/{tBlendFile} -o "
                    "$SHARED_FS_NAME'/{tBlendDIR}/frames/frame_#' -E CYCLES -F PNG -a &&\n"
                    "mpirun printf '+' >> $SHARED_FS_NAME/{tBlendDIR}/blendDone.txt\n"
                )

                torqueContext = {
                    "spTTarget": str(spDecimal),
                    "tInstance": self.instanceType,
                    "tNodes": self.numNodes,
                    "tFSNAME": self.shareName,
                    "tBlendDIR": self.destName,
                    "tBlendFile": self.blendName
                }

            else:
                torqueTemp = (
                    "#!/bin/bash\n\n"

                    "#Torque/Maui HPC Scheduler\n\n"

                    "#PBS -l nodes={tNodes}\n\n"

                    "#Shared FS is the same name specified in the CloudyCluster\n"
                    "#creation wizard when launching the cluster.\n"
                    "export SHARED_FS_NAME=/mnt/{tFSNAME} \n\n"

                    "#Blender version for Scheduler\n"
                    "module add blender/2.76\n\n"

                    "cd $SHARED_FS_NAME/blender/2.76\n"
                    "mpiexec blender -b $SHARED_FS_NAME/{tBlendDIR}/{tBlendFile} -o "
                    "$SHARED_FS_NAME'/{tBlendDIR}/frames/frame_#' -E CYCLES -F PNG -a &&\n"
                    "mpirun printf '+' >> $SHARED_FS_NAME/{tBlendDIR}/blendDone.txt\n"
                )

                torqueContext = {
                    "tNodes": self.numNodes,
                    "tFSNAME": self.shareName,
                    "tBlendDIR": self.destName,
                    "tBlendFile": self.blendName
                }

            # "newline='\n' "- needed for Windows users to make a job script
            # the same way as for Unix users.
            with open(self.blenderJS, 'w', newline="\n") as blendTorque:
                blendTorque.write(torqueTemp.format(**torqueContext))

            return True

    def sendBlend(self):
        # Makes a project folder.

        self.progressText = 'trying to mkdir ' + self.destPath + self.destName
        self.sshClient.exec_command('mkdir ' + self.destPath + self.destName)

        # Makes a frames folder.

        self.progressText = (
            'Trying to mkdir ' + self.destPath + self.destName + '/frames'
        )

        self.sshClient.exec_command(
            'mkdir ' + self.blendDest + 'frames'
        )

        if(self.videoOption is True):
            self.progressText = (
                'Trying to mkdir ' + self.blendDest + 'video'
            )
            self.sshClient.exec_command(
                'mkdir ' + self.blendDest + 'video'
            )

        time.sleep(2)

        self.scpClient = SCPClient(self.sshClient.get_transport())
        self.progressText = (
            'Copying blend file to ' + self.blendDest + self.blendName
        )
        self.scpClient.put(
            bpy.data.filepath, self.blendDest + self.blendName
        )

        self.sshClient.exec_command(
            "rm -f " + self.ccqBlender
        )

        self.progressText = (
            'Copying job script to scheduler...'
        )

        self.scpClient.put(
            self.blenderJS, self.ccqBlender
        )

        # Deleting local Blender JS copy.
        os.remove(self.blenderJS)

        return True

    def blendRender(self):

        self.sshClient.exec_command(
            "rm -f " + self.blendDest + "blendDone.txt"
        )

        time.sleep(3)

        self.sshClient.exec_command(
            "touch " + self.blendDest + "blendDone.txt"
        )

        self.sshClient.exec_command(
            'ccqsub -js ' + self.ccqBlender
        )

        # self.sshClient.exec_command('disown')
        return True

    def progressRender(self):
        # Displays progress for rendering.

        self.sftpClient = self.sshClient.open_sftp()
        self.ccFRMStart = bpy.context.scene.frame_start
        self.ccFRMEnd = bpy.context.scene.frame_end
        self.frameTOT = (self.ccFRMEnd - self.ccFRMStart) + 1

        if self.rProgress is True:
            self.rProgress = False

        while self.rProgress is False:
            stdin, stdout, stderr = self.sshClient.exec_command(
                "ls " + self.rendDest
            )
            self.sshStdout = stdout.readlines()

            self.blendDone = self.sftpClient.open(
                self.blendDest + 'blendDone.txt', 'r'
            )

            with self.blendDone as file:
                self.plusCnt = file.read()
            self.numPluses = len(self.plusCnt) - self.plusCnt.count(b'\n')
            self.nodeIdx = int(self.numNodes - self.numPluses)

            if self.rDone < 100:
                try:
                    self.sftpClient.chdir(self.rendDest)
                    for index, line in enumerate(self.sshStdout):
                        self.sshOutput = self.sshOutput + line
                        self.frameIdx = int(index + 1)
                        self.ccIndex = abs(self.frameIdx - self.nodeIdx)
                        self.rDone = int((self.ccIndex / self.frameTOT) * 100)
                    if self.rDone > 100:
                        self.progressText = ('Progress: 100%')
                        time.sleep(10)
                    else:
                        self.progressText = ('Progress: ' + str(self.rDone) + '%')
                    time.sleep(10)
                except IOError as err:
                    if err.errno == errno.ENOENT:
                        self.rDone = 0
                        self.progressText = ('Progress: ' + str(self.rDone) + '%')
                        print('Creating Resourses....please wait')
                        time.sleep(7)
            else:
                self.rProgress = True
                self.rDone = 0

        return True

    def ImageSequence(self):
        # Makes a video from a set of images.

        if(self.videoType == "MP4"):
            self.blendVid = self.destName + ".mp4"

        if(self.videoType == "MOV"):
            self.blendVid = self.destName + ".mov"

        if(self.videoType == "MPG"):
            self.blendVid = self.destName + ".mpg"

        if(self.videoType == "AVI"):
            self.blendVid = self.destName + ".avi"

        self.imgSeq = (
            "ffmpeg -i " + self.rendDest + "frame_%d.png " + self.vidDest + self.blendVid
        )

        # Time delay to ensure ffmpeg would not overload.
        time.sleep(15)

        self.progressText = (
            'Saving video file to ' + self.vidDest + self.blendVid
        )
        stdin, stdout, stderr = self.sshClient.exec_command(
            self.imgSeq
        )

        self.imgSeqStderr = stderr.readlines()

        return True

    def disconnect(self):
        self.sshClient.close()

communicator = Communicator()


class ccModalTimerOperator(bpy.types.Operator):
    # Operator which runs its self from a ccModalTimerOperator.

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
            print("finished is true.")
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
        ccShareName = context.scene.ccShareName
        ccNumNodes = context.scene.ccNumNodes
        ccSchedulerType = context.scene.ccSchedulerType
        ccSpotPrice = context.scene.ccSpotPrice
        ccSPriceAmount = context.scene.ccSPriceAmount
        ccInstanceType = context.scene.ccInstanceType
        ccVideoOption = context.scene.ccVideoOption
        ccVideoType = context.scene.ccVideoType

        # TODO: valudate the variables here
        # if anything goes wrong return False.

        ccSchCheck = urlparse(ccSchedulerURI)
        ccURegex = re.fullmatch(r"^[a-z_][a-z0-9_-]*[$]?$", ccUsername)
        ccPRegex = re.fullmatch(r"^[A-Za-z0-9_$-]+$", ccPassword)
        ccEnvCheck = ccShareName
        ccITCheck = ccInstanceType

        if ccSchCheck.path == '':
            ccvalidateMsg = "Invalid URL, it needs an IPv4 or Domain Name"
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        # Username follows basic gnu/linux name rules.
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

        # Password follows the same rules as username.
        if ccPRegex is None:
            ccvalidateMsg = ("Invalid Password! Password must be in letters, "
                             "numbers, '_', '-', or '$'!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        if len(ccPassword) > 32:
            ccvalidateMsg = ("Your password is too long, "
                             "it must be less than 32 characters!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        if ccEnvCheck == '':
            ccvalidateMsg = ("Environment name is empty. Please use the same name as "
                             "you used when you setup the environment!")
            print("Error: " + ccvalidateMsg)
            return ccvalidateMsg

        # Conditions allow ONLY if Spot Price is enabled.
        if(ccSpotPrice is True):
            if(ccITCheck == ''):
                ccvalidateMsg = ("Instance type is empty! "
                                 "You must supply a specific instance type!")
                print("Error: " + ccvalidateMsg)
                return ccvalidateMsg

        # Write valid inputs into the communicator.
        communicator.schedulerURI = ccSchedulerURI
        communicator.username = ccUsername
        communicator.password = ccPassword
        communicator.numNodes = ccNumNodes
        communicator.shareName = ccShareName
        communicator.schedulerType = ccSchedulerType
        communicator.spotPrice = ccSpotPrice
        communicator.spAmount = ccSPriceAmount
        communicator.instanceType = ccInstanceType
        communicator.videoOption = ccVideoOption
        communicator.videoType = ccVideoType

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


class ccClipboardOperator(bpy.types.Operator):
    # Operator that copy path to clipboard.
    bl_idname = "wm.ccclipboard_opt"
    bl_label = "ccClipboard Operator"

    pathMsg = "WebDav path has been copied to clipboard!"

    def execute(self, context):
        pyperclip.copy(communicator.webDavURI)
        self.report({'INFO'}, self.pathMsg)
        print(self.pathMsg)

        return {'FINISHED'}


class ccRenderPanel(bpy.types.Panel):
    # Creates the ccRender Panel.
    bl_label = 'ccRender Settings'
    bl_idname = "CC_RENDER_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = 'ccSimple_Render'

    def check(self, context):
        return communicator.progress

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        scn = context.scene
        col.label(text="Custom Interface!")

        row = col.row()
        row.prop(scn, "ccSchedulerURI")
        row = col.row()
        row.prop(scn, "ccUsername")
        row = col.row()
        row.prop(scn, "ccPassword")
        row = col.row()
        row.prop(scn, "ccShareName")
        row = col.row()
        row.prop(scn, "ccNumNodes")
        row = col.row()
        row.prop(scn, "ccSchedulerType", expand=True)

        # Spot price Checkmark 'Disables' Target Amount textbox.
        layout.prop(scn, "ccSpotPrice")
        col = layout.column()
        col.active = scn.ccSpotPrice
        row = col.row()
        row.prop(scn, "ccSPriceAmount")
        row = col.row()
        row.prop(scn, "ccInstanceType")

        col = layout.column()
        row = col.row()

        col = layout.column()
        col.label(text="Video Settings")

        # Video checkmark decides on enabling/disableing
        # video to images feature.

        layout.prop(scn, "ccVideoOption")
        col = layout.column()
        col.active = scn.ccVideoOption
        vidRow = col.row()
        vidRow.prop(scn, "ccVideoType")

        col = layout.column()
        row = col.row()

        row.operator(operator="wm.ccmodal_timer_opt", text="Begin Render")

        col = layout.column()
        col.label(text="Render Output:")
        davRow = col.row()
        davRow.label(text=str(communicator.webDavURI))

        row = col.row()
        row.operator(operator="wm.ccclipboard_opt", text="Copy Path to Clipboard")


class ccRenderVairables(bpy.types.PropertyGroup):
    blScene = bpy.types.Scene

    blScene.ccSchedulerURI = bpy.props.StringProperty(
        name="CC Scheduler URI"
    )

    blScene.ccUsername = bpy.props.StringProperty(
        name="CC Username"
    )

    blScene.ccPassword = bpy.props.StringProperty(
        name="CC Password",
        subtype='PASSWORD'
    )

    blScene.ccNumNodes = bpy.props.IntProperty(
        name="Number of render nodes",
        default=4,
        min=1,
        max=1000,
        step=1
    )

    blScene.ccShareName = bpy.props.StringProperty(
        name="CC Environment Name",
        default="efsdata"
    )

    blScene.ccSchedulerType = bpy.props.EnumProperty(
        name="Scheduler Type",
        description="Slurm or Torque/Maui",
        items=[
            ("SLURM", "Slurm", "Slurm HPC Scheduler"),
            ("TORQUE", "Torque/Maui", "Torque/Maui HPC Scheduler")
        ],
        default="SLURM"
    )

    blScene.ccSpotPrice = bpy.props.BoolProperty(
        name="Spot Pricing?",
        description="Allow Spot Pricing?",
        default=False
    )

    blScene.ccSPriceAmount = bpy.props.FloatProperty(
        name="Target Spot Price",
        description="Targeted Spot Instance Price",
        min=0.01,
        max=1000,
        step=1,
        precision=2
    )

    blScene.ccInstanceType = bpy.props.StringProperty(
        name="CC Instance Type"
    )

    blScene.ccVideoOption = bpy.props.BoolProperty(
        name="Video Output",
        description="Frame sequence images into a video (disable this if you "
        "wish to retrieve the image output ONLY.",
        default=True
    )

    blScene.ccVideoType = bpy.props.EnumProperty(
        name="Video Format",
        description="Video File Format",
        items=[
            # "ORANGE" selection helps User to ensure the video
            # format is selected.
            # Process seems to ignore this if User doesn't asign
            # a video output format.
            ("MP4", "mp4", ".mp4 format"),
            ("MOV", "mov", ".mov format"),
            ("MPG", "mpg", ".mpg format"),
            ("AVI", "avi", ".avi format")
        ],
        default="MP4"
    )


class KickoffRender(threading.Thread):

    def __init__(self, communicator, *args, **kwargs):
        super(KickoffRender, self).__init__(*args, **kwargs)
        self.communicator = communicator

        self.ccLock = Lock()

    def run(self):

        self.ccLock.acquire()
        self.communicator.render()
        self.ccLock.release()


def render():

    rdr = KickoffRender(communicator=communicator)
    rdr.start()


def make_annotations(cls):
    """Converts class fields to annotations if running with Blender 2.8+"""
    if bpy.app.version < (2, 80):
        return cls
    bl_props = {k: v for k, v in cls.__dict__.items() if isinstance(v, tuple)}
    if bl_props:
        if '__annotations__' not in cls.__dict__:
            setattr(cls, '__annotations__', {})
        annotations = cls.__dict__['__annotations__']
        for k, v in bl_props.items():
            annotations[k] = v
            delattr(cls, k)
    return cls

classes = (
    ccRenderPanel,
    ccRenderVairables,
    ccModalTimerOperator,
    ccClipboardOperator,
)

def register():
    # bpy.utils.register_class(ccRenderPanel)
    # bpy.utils.register_class(ccRenderVairables)
    # bpy.utils.register_class(ccModalTimerOperator)
    # bpy.utils.register_class(ccClipboardOperator)
    for cls in classes:
        make_annotations(cls)
        bpy.utils.register_class(cls)


def unregister():
    # bpy.utils.unregister_class(ccRenderPanel)
    # bpy.utils.register_class(ccRenderVairables)
    # bpy.utils.unregister_class(ccModalTimerOperator)
    # bpy.utils.unregister_class(ccClipboardOperator)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
