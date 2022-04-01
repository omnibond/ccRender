ccRender
========

An addon for Blender that renders a blend file to the cloud.
This uses paramiko libraries to SSH into an HPC scheduler node,
copy over the file, and evoke a job to execute Blender rendering all nodes.

Python requirements
-------------------

At the time of this instruction, the latest version of Blender is 3.1 that comes bundled with Python 3.10. You will need to make sure you are using that version of Python in order for Blender to recognize its dependencies.


Ubuntu (adjust this for Mac and other Linux Distributions)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the repository and install the python 3.10 in the terminal

::

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.10

and then download and install to the specific Python version

::

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.10 get-pip.py


Make sure you have git installed. 


Create a blender script folder for the modules and addons. Inside the script folder create the following folders:

::
    addons
    modules
    startup


Then go back to the terminal and use the following commnand to install the modules to the script modules directory:

::
    pip3.10 install --target=/home/<user>/<blenderscripts>/modules/ git+https://github.com/omnibond/ccRender


Open the modules folder inside the blender script directory. Find the folder called ``ccRender`` and move it up one level to the addons folder. 
You can move it anywhere else as long as you know where to find it in order to install ``ccSimple.py`` file that is inside ccRender.

Open Blender and find the scripts directory field in ``preferences -> file -> scripts`` and set it to the path to your <blenderscripts> folder.

Restart Blender open the addons in ``preference -> addon``. Click on ``Install to File`` button and find the python file ``ccSimple.py`` in the ccRender folder mention earlier.

Once the addon is added to Blender, enable it.

Return to the main screen, make sure you are in 3D Viewport (by default) and enable the sidebar option under View.


Windows
^^^^^^^

Once you have Blender installed, make sure Git is installed as well. You can download the latest verion on `Git for Windows
<https://git-scm.com/download/win>`_.

Open command prompt as admin and type the following:

::
    cd "[Program Directory]\Blender Foundation\Blender 3.1\3.1\python\bin"

Replae [Program Directory] with wherever you have Blender installed (default: "C:\Program Files")

Then install pip into Blender python

::
    python.exe -m ensurepip


Next, install ccRender through github (provided you should have git installed at this point):

::
    python.exe -m pip install ccRender


Once ccRender is installed, close the command prompt. Open File Explorer.
Navigate to the site-packages directory in:
::
    [Program Directory]\Blender Foundation\Blender 3.1\3.1\python\lib\site-packages

Find a folder called ``ccRender``. 
Open the folder and move the python file ``ccSimple.py`` move it to this directory:

::
    [Program Directory]\Blender Foundation\Blender 3.1\3.1\scripts\addons


If a pop-up appears asking for Administrator permissions, click "Continue". This will install the addon to Blender automatically.

Then open Blender and open the addon by ``preferences -> addon``.

Search the list of addons for ``ccRender`` to confirm the addon is enabled. If it's not enabled, enable it.

Return to the main screen, make sure you are in 3D Viewport (by default) and enable the sidebar option under View.

