ccRender
========

An addon for Blender that renders a blend file to the cloud.
This uses paramiko libraries to SSH into an HPC scheduler node,
copy over the file, and evoke a job to execute Blender rendering all nodes.

Python requirements
-------------------

Operating System's Python environment **must match** with Blender's Python environment. Currently this addon supports Python 3.5 or later. Depending on the operating system would determine the following methods for installation or verifying of Python and pip:


Ubuntu 16.04 or later
^^^^^^^^^^^^^^^^^^^^^

Python 3.x (depending what version of Ubuntu you are using) should be included by default along with pip. If pip is not installed onto your python environment, install pip onto your Python3 (not Python) using the following command:

::
   
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3 get-pip.py

Ubuntu 16.04 or later (Multiple Python Environments)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also install a different python version given it matches the version your Blender's python environment uses:

Add the repository and install the python 3.x packages (replace x to the specific version of python)

::

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.x

and then download and install to the specific Python version

::

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.x get-pip.py

Ubuntu 14.04
^^^^^^^^^^^^

Python 3.4 is included with this version and requires an upgrade to use the addon. The installation is the same as you would for multiple environments but designate your python packages to 3.5 or later.


Windows
^^^^^^^

Python 3.5 or later can be download and install directly from `Python.org <https://www.python.org/downloads/>`_. When installing, make sure that PATH option is enabled or manually add python's main directory and scripts subfolder to the PATH in the Environment Variables. 

Pip should be included with Python's installation.
If you wish to install it, download `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_ to a folder on your computer.

Open a command prompt window, preferably as Administrator, and navigate to the folder containing ``get-pip.py``.

Then run ``python get-pip.py``.


Paramiko & Pyperclip requirements
---------------------------------

Paramiko and Pyperclip has to be included into Blender's Python environment. This package includes the installation needed for both of the modules.  Ubuntu's installation differs than Windows in terms of dependencies though the installation is the same. 

Ubuntu 14.04 & 16.04 or later (pip installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the following dependencies first (replace python3.x with whatever version of python you're using if it's a later version than python 3.5) in the terminal:

::

    sudo apt-get install build-essential libffi-dev libssl-dev python3.x-dev



Create a script folder for the modules and addons, blenderscripts for example. Inside the <blenderscripts> folder, create the following folders:

::

    addons
    modules
    startup

Then go back to the terminal and use the following command to install the modules to the script modules folder:

::

    pip3 install --target=/home/<user>/<blenderscripts>/modules/ ccRender


If you are using Ubuntu 14.04 or using a different environment, the process is the same except use pip3.x instead of pip3 to ensure that the package is installing to the right python version.

Ubuntu 14.04 & 16.04 or later (Github installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to install the modules through Github, the process is similar. Install the same dependencies as it is for pip, but include the following dependency:

::

    git-core

Then use the following command after creating the folders (pip3.x instead of pip3 if using Ubuntu 14.04 or later version with different environment):

::

    pip3 install --target=/home/<user>/blenderscripts/modules/ git+https://github.com/omnibond/ccRender

Windows (Github installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before installing the package from GitHub, Git must be installed. You can download and install the latest version on from Git website under `Git for Windows
<https://git-scm.com/download/win>`_.


Create a blender script folder, preferably in the Documents folder, and create the following folders inside <blenderscripts>:

::

    addons
    modules
    startup

Then open up command panel as Administrator and pip install ccRender into the modules folder

::

    pip install --target=C:\Users\<username>\Documents\blenderscripts\modules\ git+https://github.com/omnibond/ccRender

Windows (PyPi installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to install the modules using PyPi, the process is the same. use this command in the command panel as Administrator:

::

    pip install --target=C:\Users\<username>\Documents\blenderscripts\modules\ ccRender


Windows 10 & 11 (Bash Method)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Windows 10 and 11 users that have Linux Bash Shell enabled, can follow the instructions listed for Ubuntu. The pip installation process is similar, make note towards the directory path such as the example below:

::

    pip install --target=/mnt/c/Users/<username>/Documents/<blenderscripts>/modules/ ccRender

Those who wish to install the addon through Github instead of PyPi, will need to make sure that Git is installed. Installing the addon onto Blender is the same as the other Windows installations.


Setup Blender addon
-------------------

An additional folder, called ``ccrender`` will be installed to the same location as Paramiko and Pyperclip. This folder can be moved to addons. If it's not there, download it from Github, and move it to the addons folder in <blenderscripts>. Before installing the python file, you'll need to set the script directory to your <blenderscripts> folder.

Blender 2.80 or later
^^^^^^^^^^^^^^^^^^^^^
To set the script folder, open Blender. Then find the scripts directory field in ``Edit -> Preferences -> File Paths`` and set the value to the path to your <blenderscripts> folder.

Then to install the addon to Blender, install the python file in ``Edit -> Preferences -> Add-ons-> Install`` and find the addon called ``ccSimple.py`` in the ccRender folder in your <blenderscripts> folder (preferably in the addons).

Once the addon is installed, enable the addon. Your setting will be saved automatically

Return to the main screen, make sure you are in 3D Viewport and enable the sidebar under View.

Blender 2.78
^^^^^^^^^^^^
To set the script folder, open Blender. Then find the scripts directory field in ``preferences -> file -> scripts`` and set the value to the path to your <blenderscripts> folder.

Restart Blender and install the python file in ``preferences -> addon -> install to file`` and find the addon called ``ccSimple.py`` in the ccRender folder in your <blenderscripts> folder (preferably in the addons).

Once the addon is installed, enable the addon and save user settings.
