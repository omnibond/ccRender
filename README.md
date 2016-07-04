# ccRender
An addon for blender that renders the current .blend file in the cloud.  This uses paramiko libraries to ssh into an HPC scheduler node (like those provided with CloudyCluster), copy over a .blend, and envoke a job to execute blender on all nodes.

## Paramiko requirements
Paramiko has to be included into blender's python environment.  To get this to work in Ubuntu I've had to use pip to install paramiko and it's dependencies into a local target using the target command:

```bash
mkdir /usr/share/blender/scripts/modules/pipmodules
pip install paramiko --target=/usr/share/blender/scripts/modules/pipmodules
```
and then restart blender.
