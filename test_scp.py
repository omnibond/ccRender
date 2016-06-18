import paramiko
from scp import SCPClient

sshClient = paramiko.SSHClient()
sshClient.load_system_host_keys()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = "lsketch-bixbitebearcobia.cloudycluster.com"
username = "craigb"
password = "Clblc11823"
port = 22
blendPath = '/home/craigb/Downloads/'
blendFileName = 'cards-cycles.blend'
destinationPath = '/home/craigb/'
sshClient.connect(hostname,port,username,password)

name = blendFileName.split('.')
name = name[0]

print('trying to mkdir '+destinationPath+name)
sshClient.exec_command('mkdir '+destinationPath+name)
print('trying to mkdir '+destinationPath+name+'/frames')
sshClient.exec_command('mkdir '+destinationPath+name+'/frames')
# SCPCLient takes a paramiko transport as its only argument
scpClient = SCPClient(sshClient.get_transport())
print('copying blend file to '+destinationPath+name+'/'+blendFileName)
scpClient.put(blendPath+blendFileName, destinationPath+name+'/'+blendFileName)

scpClient.close()