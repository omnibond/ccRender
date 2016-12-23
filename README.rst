ccRender
========

An addon for blender that renders the current .blend file in the cloud.
This uses paramiko libraries to ssh into an HPC scheduler node (like
those provided with CloudyCluster), copy over a .blend, and envoke a job
to execute blender on all nodes.

Python requirements
-------------------
Python in the operating system **must match** with the current python version that Blender uses. Currently python 3.5 is supported until Blender updates that will use the latest python version. Depending on the operating system would determine the following methods for instalation or verifying of python and pip:

Ubuntu 16.04

Python 3.5 should be included by default, however python3's pip might not be. To install pip onto your python3 (not python), use the following command:

::
   
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3 get-pip.py


Ubuntu 14.04

Python 3.4 is included with this version and requires an upgrade to use the addon. To install the latest version of python and add pip:

Add the repository and install the python 3.5 packages

::

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.5 python3.5-dev

and then download and install pip to the specific python version (e.g. python3.5)

::

   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3.5 get-pip.py


Windows

Python 3.5 can be download and install directly from `Python.org
<https://www.python.org/downloads/release/python-352/>`_. When installing, make sure that PATH option is enabled or manually add python's main directory and scripts subfolder to the PATH in the Environment Vairables.


Paramiko requirements
---------------------

Paramiko has to be included into blender's python environment. This package include the installation needed for paramiko.  Ubuntu's installation differs than Windows in terms of dependecies though the installation is the same.: 

Ubuntu 14.04 & 16.04

Install the following dependecies first.
::

    sudo apt-get install build-essential libffi-dev libssl-dev zlib1g-dev


Then use the following commands:
::
    
    mkdir /home/user/blenderscripts
    mkdir /home/user/blenderscripts/addons
    mkdir /home/user/blenderscripts/modules
    mkdir /home/user/blenderscripts/startup
    pip3 install --target=/home/user/blenderscripts/modules/ ccRender

and then set the value in preferences -> file -> scripts to

::

    /home/user/blenderscripts

and restart blender.


Windows


Create blenderscripts folder preferably in the Documents folder and create the following folders inside blenderscripts:

::

    addons
    modules
    startup

Then pip install ccRender into the modules folder

::
    pip install --target=C:\Users\username\Documents\blenderscripts\modules\ ccRender

and then set the value in preferences -> file -> scripts to

::

    C:\Users\username\Documents\blenderscripts

and restart blender.