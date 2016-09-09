import os
import paramiko
import time
import socket
from scp import SCPClient

# d = bpy.data
# p = bpy.path

sshClient = paramiko.SSHClient()
sshClient.load_system_host_keys()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = "xxx.xxx.xxx.xx"
username = "cliff"
password = "******"
port = 22
sshClient.connect(hostname, port, username, password)
# username = "cliff"

lFilepath = "/home/cliff/Documents/blender/test_script/test_script1.sh"

dir_path = os.path.dirname(lFilepath)
dir_name = os.path.basename(lFilepath)
destPath = '/home/' + username + '/'
destName = os.path.splitext(os.path.basename(lFilepath))[0]
# destName = p.display_name_from_filepath(d.filepath)

# print(dir_path)
# print(dir_name)
# print(destName)

print("tyring to mkdir " + destPath + destName)
sshClient.exec_command('mkdir ' + destPath + destName)

# time.sleep(2)
# print("creating 'frames folder " + destPath + destName + "/frames")

time.sleep(2)
scpClient = SCPClient(sshClient.get_transport())
print('copying blend file to ' + destPath + destName + '/' + dir_name)
scpClient.put(lFilepath, destPath + destName + '/' + dir_name)

print("complete")
scpClient.close()

print('Executing blend file ' + dir_name)
sshClient.exec_command("chmod a+x " + destPath + destName + '/' + dir_name)
sshClient.exec_command('/' + destPath + destName + '/' + dir_name)
