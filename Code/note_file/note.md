# IMPORTANT!!!! Add the function in DayTask to show the time_conversion for all the activities of that DayTask (for loop to iterate through the activities in the list)

# Can use QComboBox for the time_conversion button

# Create the help function for app

We can use the tooltip in PyQt5: https://zetcode.com/gui/pyqt5/firstprograms/. 

When the mouse hover over a button, the program can show the usage and purpose of the button. 

**ctrl-f**: "Showing a tooltip in PyQt5".

# ~~Message box confirm exit the program~~

Ask to confirm before allow the user exit the program: https://zetcode.com/gui/pyqt5/firstprograms/

*Possible: Upgrade to "not ask again" in the message box*

**ctrl-f**: "PyQt5 message box"

# Show time on the screen

Some code from `gui.py` from round 6 `robots` exercise.

```
# Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_robots)
        self.timer.start(10) # Milliseconds
```

# ~~Menubar for the program~~

Everything from menubar, sub menu, check menu (e.g., toggle to show something)

https://zetcode.com/gui/pyqt5/menustoolbars/

**ctrl-f**:"PyQt5 simple menu"


# ~~Layout of the program~~

https://zetcode.com/gui/pyqt5/layout/

Useful examples: 
- QHBoxLayout and QVBoxLayout for responsive layout within the program
- GridLayout + span columns/rows: quite similar to CSS Grid (**PREFER**)
- QLineEdit, QTextEdit

# LCD Display and SLider

https://zetcode.com/gui/pyqt5/eventssignals/

# Possible way of getting the activity name from user

QInputDialog. A box appears to get the input from user and show in the text editor.

**ctrl-f**: "PyQt5 QInputDialog"

We can also add color to the activity

**ctrl-f**: "PyQt5 QColorDialog"

**Open file**: "PyQt5 QFileDialog"

- Many more cool features that can be added to the program: change the font, open file from computer
  - https://zetcode.com/gui/pyqt5/dialogs/
- Splitter: a box which can be resize accordingly (example_pyqt5/splitter.py)
  - https://zetcode.com/gui/pyqt5/widgets2/
- Combo Box: like a drop list choice (example_pyqt5/combobox.py)
  - https://zetcode.com/gui/pyqt5/widgets2/

create the Calendar Widget for the user to pick up the date of the activity (have the today button so that they can choose today easily)

# A timer using QTimer example

https://pythonpyqt.com/qtimer/

# IMPORTANT - About how the program initially runs and then the choose day/next day function works along

### First, we need to understand the architecture of the OOP of the program:

The OOP works: AllTask -> DayTask -> Activity

AllTask will work like a central database of the whole program. It is a outermost, biggest container, and it contains the DayTask objects.

The DayTask are smaller containers, and they are distinguished by the date. Each DayTask object has an unique date. They contain the Activity objects. This class will also be the class to show on the GUI.

The Activity class represents the activity that user want to keep track of the time spent. Each Activity class will have a name, timer, and the DayTask that it belongs to.

### The workflow of the program

When the program opens, it will create a new object DayTask with the date of today(). Then that DayTask object is added to the AllTask object.

When the user chooses the choose day/next day function, the program can read the data of that day and open a new window for the new day user choose.

Links: 
- https://www.google.com/search?q=how+to+create+a+button+that+pop+up+another+page+when+clicked+pyqt&oq=how+to+create+a+button+that+pop+up+another+page+when+clicked+pyqt&aqs=chrome..69i57.14907j0j7&sourceid=chrome&ie=UTF-8

- https://www.pythonguis.com/tutorials/creating-multiple-windows/

# Add a pop up note for Export function about "Export file is in CSV type and best viewed with Excel. For visualizing data use Stats function of the program instead. WARNING: DO NOT edit the exported CSV file!"

# Save file when exit:

The beginning of the link:
https://doc.qt.io/qt-5/qmessagebox.html

