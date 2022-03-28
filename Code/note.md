### Create the help function for app

We can use the tooltip in PyQt5: https://zetcode.com/gui/pyqt5/firstprograms/. 

When the mouse hover over a button, the program can show the usage and purpose of the button. 

**ctrl-f**: "Showing a tooltip in PyQt5".

### Message box confirm exit the program

Ask to confirm before allow the user exit the program: https://zetcode.com/gui/pyqt5/firstprograms/

*Possible: Upgrade to "not ask again" in the message box*

**ctrl-f**: "PyQt5 message box"

### Show time on the screen

Some code from `gui.py` from round 6 `robots` exercise.

```
# Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_robots)
        self.timer.start(10) # Milliseconds
```

### Menubar for the program

Everything from menubar, sub menu, check menu

https://zetcode.com/gui/pyqt5/menustoolbars/

**ctrl-f**:"PyQt5 simple menu"

