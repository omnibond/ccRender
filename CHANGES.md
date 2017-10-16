# Changelog

## 0.11.1 (2017-10-15)
- Fixed issue that prevents executing the addon multiple times without closing and reopening Blender.
- Repeated progress now show correct percentage while CCQ script is executing.

## 0.11.0 (2017-9-17)
- Added Image Sequence feature to UI.
- User will now be able to allow or disable Image Sequencing. By defualt, Image Sequencing is enabled and after rendering, the rendered images are gathered and stitched togeter into a video of the user's choice.
-The following video formats are now available: MP4, MOV, MPG, & AVI.
-Updated script to suit the webdav link to the video output (if Image Sequencing is enabled) or the rendered frames folder.
-Updated Reademe.rst to include an alternative installation for Windows 10 Users who have Windows Subsystem for Linux enabled. 

## 0.10.0 (2017-7-19)
- Added Spot Instance feature to UI.
- User will now be able to choose if they want spot instance nor not. If they do, they must supply the target amount, and the instance type before they start rendering.
- Updated script to suit both spot instance and non-spot instance
- Added render output to both console and UI.
- Added copy to clipboard button. User can now copy render output link to clipboard on the UI as an alternative to copy it from console.
- Updated Readme.rst to include instructions for installing pyperclip module and option for user to install the required modules via pip instead of Github.

## 0.9.0 (2017-6-16)
- Added Environment Name to UI to specify their shared envirionment.
- Added a process that writes out a slurm job script template as a local script file. Then the script file is copied to the scheduler where the addon would ssh to that file to begin rendering. The local script is removed after it's sent a copy to the the scheduler.
- Updated ssh command according to CCQ parameters for rendering process.

## 0.8.4 (2017-4-21)
- Changed description in blender info.

## 0.8.3 (2017-4-19)

- Changed "Currently" to "Progress" in progressRender.
- Clean up addon for clarity.
- Updated Readme.rst for clarification.

## 0.8.2 (2017-4-7)

- Updated render process to accurate involve nodes and number of pluses in blendDone.txt file.

## 0.8.1 (2017-3-17)

- Add render progress to the View header.

## 0.7.0 (2017-1-6)

- Add changelog.
- Added threadding Lock.
- Tread lock should work against race conditions easily recgonized on VM.
- Removed __init__.py from tests folder and main directory.
- Updated README.rst to include Git installation.