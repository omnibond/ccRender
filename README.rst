ccRender
========

An addon for Blender that renders a blend file to the cloud. This uses paramiko libraries to SSH into an HPC scheduler node, copy over the file, and envoke a job to execute Blender rendering all nodes.

Python requirements
-------------------

Operating System's Python envirionment **must match** with Blender's Python envirionment. Currently this addon supports Python 3.5. Depending on the operating system would determine the following methods for instalation or verifying of Python and pip:

Ubuntu 16.04
^^^^^^^^^^^^

Python 3.5 should be included by default, however Python3's pip might not. To install pip onto your Python3 (not Python), use the following command:

::
   
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3 get-pip.py


Ubuntu 14.04
^^^^^^^^^^^^

Python 3.4 is included with this version and requires an upgrade to use the addon. To install the latest version of Python and add pip:

Add the repository and install the Python 3.5 packages

::

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.5

and then download and install pip to the specific Python version (e.g. Python 3.5)

::

   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3.5 get-pip.py


Windows
^^^^^^^

Python 3.5 can be download and install directly from `Python.org <https://www.python.org/downloads/release/python-353/>`_. When installing, make sure that PATH option is enabled or manually add python's main directory and scripts subfolder to the PATH in the Environment Vairables. 

Pip should be included with Python's installation. If you wish to install it, download `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_ to a folder on your computer.

Open a command prompt window, preferably as Administrator, and navigate to the folder containing ``get-pip.py``.

Then run ``python get-pip.py``.


Paramiko & Pyperclip requirements
---------------------------------

Paramiko and Pyperclip has to be included into Blender's Python environment. This package includes the installation needed for both of the modules.  Ubuntu's installation differs than Windows in terms of dependencies though the installation is the same. 

Ubuntu 14.04 & 16.04
^^^^^^^^^^^^^^^^^^^^

Install the following dependencies first.
::

    sudo apt-get install build-essential libffi-dev libssl-dev python3.5-dev


Then use the following commands:
::
    
    mkdir /home/<user>/blenderscripts
    mkdir /home/<user>/blenderscripts/addons
    mkdir /home/<user>/blenderscripts/modules
    mkdir /home/<user>/blenderscripts/startup
    pip3 install --target=/home/<user>/blenderscripts/modules/ ccRender

If you wish to install them through Github, the process is similar. You will need to install the following dependency:
::

    git-core

Then use the following command after creating the folders :
::

    pip3 install --target=/home/<user>/blendscripts/modules/ git+https://github.com/omnibond/ccRender


If you are using Ubuntu 14.04, the process is the same except use pip3.5 instead of pip3 to ensure that the package is installing to the right Python version.

Open Blender and set the value in ``preferences -> file -> scripts`` to

::

    /home/<user>/blenderscripts

and restart Blender.

An additional folder, called ``ccrender`` will be installed to the same location as Paramiko and Pyperclip. This can be moved to the addons folder but it's optional. To install it onto Blender, install the Python file in ``preferences -> addon -> install to file`` and find the addon in:

::

    /home/<user>/blenderscripts/addons/ccrender/ccSimple.py

Then enable the addon and save user settings.


Windows
^^^^^^^
Before installing the package from GitHub, Git must be installed. You can download and install the latest version on from Git website under `Git for Windows
<https://git-scm.com/download/win>`_.


Create the blenderscripts folder, preferably in the Documents folder, and create the following folders inside blenderscripts:

::

    addons
    modules
    startup

Then open up command panel as Administrator and pip install ccRender into the modules folder

::

    pip install --target=C:\Users\<username>\Documents\blenderscripts\modules\ git+https://github.com/omnibond/ccRender

Then open Blender and set the value in ``preferences -> file -> scripts`` to

::

    C:\Users\<username>\Documents\blenderscripts

and restart Blender.

The process is the same for installation through PyPi. Use this command in the command panel as Administrator:
::

    pip install --target=C:\Users\<username>\Documents\blenderscripts\modules\ ccRender

An additional folder, called ``ccrender`` will be installed to the same location as Paramiko and Pyperclip. This can be moved to the addons folder but it's optional. To install it onto Blender, install the Python file in ``preferences -> addon -> install to file``  and find the addon in:

::

    C:\Users\<username>\Documents\blenderscripts\addons\ccrender\ccSimple.py

Then enable the addon and save user settings.

Windows 10
----------

Windows 10 users that have Linux Bash Shell enabled, can follow the instructions listed for Ubuntu. The pip installation process is similar, make note towards the directory path such as the example below:

::

    pip install --target=/mnt/c/Users/<username>/Documents/blenderscripts/modules/ ccRender

Those who wish to install the addon through Github instead of PyPi, will need to make sure that Git is installed. Installing the addon onto Blender is the same as the other Windows installations.