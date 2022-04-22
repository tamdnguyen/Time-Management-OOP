from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QFormLayout, QDesktopWidget, QLabel, QHBoxLayout

from PyQt5.QtCore import pyqtSignal

class PomodoroSettingGUI(QDialog):
    """
    The class PomodoroSettingGUI creates a dialog that asks for the setting of pomodoro from the users. 
    The dialog includes a label introducing about Pomodoro Technique, and then it asks for 2 inputs:
        - worktime
        - resttime
    """
    accepted = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.init_windows()
        self.init_UI()

    
    def init_UI(self):
        """
        This method creates a layout and add the widgets to the pop up window dialog

        The layout will be QFormLayout, and the form will include:
            - label with an instruction about the pomodoro technique
            - input for worktime
            - input for resttime
            - Buttons layout: 2 button OK + Cancel
        """

        # Label for instruction
        self.introduction = QLabel("The Pomodoro Technique was invented in the early 1990s by developer, entrepreneur, and author Francesco Cirillo. The methodology is simple: When faced with any large task or series of tasks, break the work down into short, timed intervals (called “Pomodoros”) that are spaced out by short breaks.<br><br>\
        Five steps to get started with Pomodoro:\
            <ol>\
                <li>Choose a task to be accomplished.</li>\
                <li>Set the Pomodoro to 25 minutes (the Pomodoro is the timer).</li>\
                <li>Work on the task until the Pomodoro rings, then put a check on your sheet of paper.</li>\
                <li>Take a short break (5 minutes is OK).</li>\
                <li>Every 4 Pomodoros take a longer break (25-30 minutes).</li>\
            </ol>\
        However, the default 25-5 setting is too short for some people (e.g., they prefer longer periods like 50-10). Therefore, this app allows the users to choose their suitable workng time and rest time.")
        self.introduction.setWordWrap(True)

        # Input for worktime
        self.worktime = QLineEdit()
        self.worktime.textEdited[str].connect(self.unlock)

        # Input for resttime
        self.resttime = QLineEdit()
        self.resttime.textEdited[str].connect(self.unlock)

        # Button layout with 2 buttons: OK + Cancel
        self.button_layout = QHBoxLayout()

        self.ok_btn = QPushButton('OK')
        self.ok_btn.setDisabled(True)
        self.ok_btn.clicked.connect(self.ok_pressed)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.button_layout.addWidget(self.ok_btn)
        self.button_layout.addWidget(self.cancel_btn)

        # create the layout of the app and add the rows to the layout
        form = QFormLayout(self)
        form.addRow(self.introduction)
        form.addRow('Working Time (min)', self.worktime)
        form.addRow('Resting Time (min)', self.resttime)
        form.addRow(self.button_layout)


    def checked_worktime(self, qlineedit):
        """
        This method checks if the worktime input has been filled in or not
        
        Return:
            - True if the worktime QLineEdit has been filled
            - False otherwise
        """
        if qlineedit.text() != "":
            return True
        else:
            return False

    
    def checked_resttime(self, qlineedit):
        """
        This method checks if the resttime input has been filled in or not
        
        Return:
            - True if the resttime QLineEdit has been filled
            - False otherwise
        """
        if qlineedit.text() != "":
            return True
        else:
            return False


    def unlock(self):
        """
        This method unlock the OK button when both worktime and resttime QLineEdit are filled in"""
        if self.checked_worktime(self.worktime) and self.checked_resttime(self.resttime):
            self.ok_btn.setEnabled(True)
        else:
            self.ok_btn.setDisabled(True)


    def ok_pressed(self):
        """
        This method executes the window and sends the pomodoro setting information when the OK button is pressed
        """
        pomodoro_settings = {'worktime': self.worktime.text(),
                  'resttime': self.resttime.text()}
        self.accepted.emit(pomodoro_settings)
        self.accept()


    def init_windows(self):
        """
        This method set the windows of the app
        and put it in the center of the screen
        """
        self.resize(450, 450)
        self.center()

        self.setWindowTitle('Help Information')
        #self.show()

    
    def center(self):
        """
        This method centers the window on the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


"""
The lines below are for testing this GUI

class Template(QWidget):

    def __init__(self):
        super().__init__()
        dg = PomodoroSettingGUI()
        dg.accepted.connect(self.do_something)
        dg.exec_()

    def do_something(self, values):
        print(values['File'], values['Date'], values['Printer'])


app = QApplication(sys.argv)
gui = Template()
sys.exit(app.exec_())


def main():
    app = QApplication(sys.argv)
    settng = PomodoroSettingGUI()
    print(settng.accepted)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
"""

