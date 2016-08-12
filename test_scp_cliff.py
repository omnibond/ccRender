import bpy
import os
import paramiko
import socket
from scp import SCPClient

d = bpy.data
p = bpy.path

sshClient = paramiko.SSHClient()
sshClient.load_system_host_keys()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = "********"
username = "cliff"
password = "********"
port = 22

blendDir = os.path.dirname(d.filepath)
blendFileName = p.basename(d.filepath)
destinationPath = '/home/' + username + '/'
destName = p.display_name_from_filepath(d.filepath)

sshClient.connect(hostname, port, username, password)

# try:
#     sshClient.connect(hostname, port, username, password)

# except paramiko.BadHostKeyException as err:
#     print("Bad Host Key")
#     return {"CANCELED"}
# except paramiko.AuthenticationException as err:
#     print("Authenication Error")
#     return {"CANCELED"}
# except paramiko.SSHException as err:
#     print("SSH Connection failed: " + err)
#     return {"CANCELED"}
# except socket.error as err:
#     print("SSH Connection failed: " + err)
#     return {"CANCELED"}


if not blendDir:
    print("Error: Save file first")

print("trying to mkdir " + destinationPath + destName)
sshClient.exec_command('mkdir ' + destinationPath + destName)

scpClient = SCPClient(sshClient.get_transport())
print('copying blend file to ' + destinationPath + destName + '/' + blendFileName)
scpClient.put(d.filepath, destinationPath + destName + '/' + blendFileName)

print('complete!')

scpClient.close()
