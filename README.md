# Time management OOP

## Checkpoint 2 - 15.04.2022

The GUI is complete. Program is completed around 60-70%. Some functions of the program are not yet implemented and cannot be used.

## Getting Started

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

## Usage

#### If you are a GUI type person and would like to use the code editors (Recommended method)

In your code editor, open the folder `Time-Management-OOP`. In folder `Code`, open and run the file `main.py` to start the program. That's it, enjoy the program.

#### If you are a terminal type person

In the terminal, `cd` to folder `Time-Management-OOP`. Run the commands below:

```
$ cd Code
$ python main.py
```


## Current properties

The GUI is completed and can be used easily. Currently, the `main` function is written in a testing style, so the program works is not 100% ready.

However, some basic things can be done now. For example, the users can add/delete/edit the activities. The users can also start, stop, reset, restart the timer. There is also a `Time Conversion` button so that the users can choose the time expression they like.
 
## What to do next?

Connect all the buttons on the GUI to the backend to add functionality for them. Add color, decoration so that the program is more user-friendly.

- [x] ~~Import/Export the time management data~~
- [x] ~~Unittest~~
- [ ] GUI | Connect to the backend
- [x] ~~Main workflow~~
- [ ] Pomodoro and reminder to take a break | Modify the return and workflow
- [ ] Moving to next day function [?]
- [ ] Choose the day to show function
- [x] ~~Loading a file to the program function **Same as the Import function**~~
- [x] ~~Edit and Delete function~~

## Some current limitation (bugs) of the app

At the moment, the app still has some small limitations that can be noticed during the use (it does not work perfectly as the apps on the market). However, many improvements can be made to the app in the future. Some of the limitations that have been noticed so far include:
- User creates 2 activities with the same name is now still possible in the app. One improvement can be creating a pop up windows to ask if the person wants to rename the activity or not.
- User cannot hold and change the position of the activities in the GUI
- After deleting the activities, the GUI display shows wrong information.

## Reference

- Stopwatch in Python (for class Timer): https://github.com/ravener/stopwatch.py
- PyQt5 GUI tutorial: https://zetcode.com/gui/pyqt5/


Last update: 15.04.2022

Happy Learning! Cheers!
