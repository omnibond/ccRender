# ccRender
An addon for blender that renders the current .blend file in the cloud.  This uses paramiko libraries to ssh into an HPC scheduler node (like those provided with CloudyCluster), copy over a .blend, and envoke a job to execute blender on all nodes.

## Paramiko requirements
Paramiko has to be included into blender's python environment.  To get this to work in Ubuntu I've had to use pip to install paramiko and it's dependencies into a local target using the target command:

```
mkdir /home/user/blenderscripts
mkdir /home/user/blenderscripts/addons
mkdir /home/user/blenderscripts/modules
mkdir /home/user/blenderscripts/startup
pip install --target=/home/craigb/blenderscripts/modules/ git+https://github.com/jbardin/scp.py
```
and then set the value in preferences -> file -> scripts to 
```
/home/user/blenderscripts
```
and restart blender.
