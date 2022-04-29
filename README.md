# Time management OOP

Demo video of the program [here]().

## Table of Content

1. [Introduction](#introduction)
2. [Installation Instructions](#installation-instructions)
3. [User Instructions](#user-instructions)
4. [Reference](#reference)

## Introduction <a id="introduction"></a>

Time Management is a program that allows the users to measure the time of their activities (same mechanism with stopwatch). The program offers different functionality and flexibility for users' need and favor. 

- Users can measure the time of up to 5 activities simultaneously. 
- The basic operations include start/resume, stop/pause, reset, restart the timer of the activities. 
- The users can also edit the activity name or delete the activity from the program. 
- Besides, the user can choose the time expression they want, export data, move to next day and choose any day they want to measure the time.
- The unique features of the program are Statistics, Pomodoro and Help:
  - Statistics can show the overview of the program data, some descriptive data and the visualization from the time measurement. 
  - Pomodoro allows the users to freely set their Pomodoro reminder, and sends the notification about working/resting based on Pomodoro technique. 
  - Help feature shows the information and guidance to the users.

## File and Directory Structure

The file and directory structure looks like this:

```
|__ .idea
|
|__ Code
|
|__ Document
|
|__ README.md
|
|__ requirements.txt
```

- Folder `.idea` is automatically generated by IDE and not needed to read. 
- Folder `Code` includes the code files of the project. Read the files following the instructions below:
  - The `.py` files (1) at the root of the `Code` folder are basically the main files that are used to create the `Time Management app`. Files `draft_test.py` and `timer_gui.py` are draft files and can be skipped.
  - Folder `tests` includes the unittest files which test different classes of the program.
  - Other folders can be skipped. **Note:** *folder `example_pyqt5` contains different PyQt5 library examples which are not written by the author of this program. The usage of PyQt5 in the code files (1) are not directly copied from these examples.*
- Folder `Document` contains all the documentation of the projects include `Project Plan` and `Project Document`. There is no need to read other files inside this folder.
- `README.md` file is used for writing the instruction of the project.
- `requirements.txt` file contains the external libraries that the program uses. It is conveniently used for installing and running program (see section [Installation Instruction](#installation-instructions) below for more details)

## Installation Instructions <a id="installation-instructions"></a>

### Python3

 - Python3 can be downloaded from [Python Official website](https://www.python.org/downloads/) (Python 3.9 is recommended)

### Code Editor (Optional)

A code editor is not mandatory to run the program, but it is nice to have one. Here are some recommended code editors:
- Visual Studio Code: download [here](https://code.visualstudio.com/download)
- PyCharm: download [here](https://www.jetbrains.com/pycharm/download/#section=windows)
- Some other popular code editors: Sublime Text, Vim, etc.

### Install

In your terminal (command prompt in Windows), change directory to the project folder and run the following commands:

- For TAs and teacher of the course

```
$ git clone https://version.aalto.fi/gitlab/nguyent99/time-management-oop.git
$ cd Time-Management-OOP
$ pip install -r requirements.txt
```
- For other users

```
$ git clone https://github.com/tamdnguyen/Time-Management-OOP.git
$ cd Time-Management-OOP
$ pip install -r requirements.txt
```

**NOTE:** If some errors happen while trying to install the external libraries or running the program, here are the list of libraries along with instruction of installing them:
- [numpy](https://numpy.org/install/) (This library is not allowed, and also not used in the project, but it is a required library for installing `pyqtgraph` library)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyQt5-Qt5](https://pypi.org/project/PyQt5-Qt5/)
- [PyQt5-sip](https://pypi.org/project/PyQt5-sip/)
- [PyQtChart](https://pypi.org/project/PyQtChart/)
- [PyQtChart-Qt5](https://pypi.org/project/PyQtChart-Qt5/)
- [pyqtgraph](https://pypi.org/project/pyqtgraph/)

## User Instructions <a id="user-instructions"></a>

### If you are a GUI type person and would like to use the code editors (Recommended method):

In your code editor, open the folder `Time-Management-OOP`. In folder `Code`, open and run the file `main.py` to start the program. That's it, enjoy the program.

<br>

### If you are a terminal type person:

In the terminal, `cd` to folder `Time-Management-OOP`. Run the commands below:

```
$ python3 Code/main.py
```


## Reference <a id="reference"></a>

- Stopwatch in Python (for class Timer): https://github.com/ravener/stopwatch.py
- PyQt5 GUI tutorial: https://zetcode.com/gui/pyqt5/


Last update: 29.04.2022

Happy Learning! Cheers!
