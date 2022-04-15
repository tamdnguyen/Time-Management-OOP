# Time management OOP

## Checkpoint 2 - 15.04.2022

The GUI is complete. Program is completed around 60-70%. Some functions of the program are not yet implemented and cannot be used.

## Getting Started

### Python3

 - Python3 can be downloaded from [Python Official website](https://www.python.org/downloads/) (Python 3.9 is recommended)

### Code Editor (OPTIONAL)

A code editor is not mandatory to run the program, but it is nice to have one. Here are some recommended code editors:
- Visual Studio Code: download [here](https://code.visualstudio.com/download)
- PyCharm: download [here](https://www.jetbrains.com/pycharm/download/#section=windows)
- Some other popular code editors: Sublime Text, Vim, etc.

### Install

In your terminal (command prompt in Windows), change directory to the project folder and run the following commands:

```
$ git clone https://github.com/tamdnguyen/Time-Management-OOP.git
$ pip install -r requirements.txt
```




## Current properties

Some main classes of the program has been implemented:
- `Activity` class
- `Timer` class
- `Date` class
- `TimeConversion` class

Currently, the program can create the tasks and track its time. However,
the time tracking is still not automatic, I could only test the tracking
feature using `time.sleep()` function.

The time display can also be chosen by the users. There are currently
4 different choices of time display.


## Instructions

 - Is it possible to run the program already? No. However, a main function
can be written to run the program at the most basic level (i.e., add activities
, automatically track time of the activities, choose different time display)
 - How is the program executed? For the most basic execution of the program,
a very simple `main` function has been written. This function creates a task,
and track its time using the `time.sleep()` function. To execute this `main`,
go to folder Code, run the file `main.py`

## Schedule

 - How much time have you spent making the project this far? More than three full days
 - Have you made changes to the schedule of your project plan?

## Other

 - Have you faced any specific problems? At first, I was lost at implementing the main classes
 - Have you had to make changes to your plan?
 
## What to do next?

- [x] ~~Import/Export the time management data~~
- [x] ~~Unittest~~
- [ ] GUI | Connect to the backend
- [ ] Main workflow
- [ ] Pomodoro and reminder to take a break | Modify the return and workflow
- [ ] Moving to next day function [?]
- [ ] Choose the day to show function
- [x] ~~Loading a file to the program function **Same as the Import function**~~
- [x] ~~Edit and Delete function~~

## Some current limitation (bugs) of the app

At the moment, the app still has some small limitations that can be noticed during the use (it does not work perfectly as the apps on the market). However, many improvements can be made to the app in the future. Some of the limitations that have been noticed so far include:
- User creates 2 activities with the same name is now still possible in the app. One improvement can be creating a pop up windows to ask if the person wants to rename the activity or not.
- User cannot hold and change the position of the activities in the GUI

## Reference

- Stopwatch in Python (for class Timer): https://github.com/ravener/stopwatch.py
- PyQt5 GUI tutorial: https://zetcode.com/gui/pyqt5/


Last update: 13.04.2022

Happy Learning! Cheers!
