# Create the help function for app

We can use the tooltip in PyQt5: https://zetcode.com/gui/pyqt5/firstprograms/. 

When the mouse hover over a button, the program can show the usage and purpose of the button. 

**ctrl-f**: "Showing a tooltip in PyQt5".

# Message box confirm exit the program

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

# Menubar for the program

Everything from menubar, sub menu, check menu (e.g., toggle to show something)

https://zetcode.com/gui/pyqt5/menustoolbars/

**ctrl-f**:"PyQt5 simple menu"


# Layout of the program

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
