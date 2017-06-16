# Changelog

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