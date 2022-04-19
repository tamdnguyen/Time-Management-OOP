import sys

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QDateEdit, QFormLayout, QWidget, QDesktopWidget, QLabel

from PyQt5.QtCore import QDate, pyqtSignal

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
        """
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

        self.worktime = QLineEdit()
        self.worktime.textEdited[str].connect(self.unlock)

        self.resttime = QLineEdit()
        self.resttime.textEdited[str].connect(self.unlock)

        self.ok_btn = QPushButton('OK')
        self.ok_btn.setDisabled(True)
        self.ok_btn.clicked.connect(self.ok_pressed)

        self.cancel_btn = QPushButton("Cancel")

        form = QFormLayout(self)
        form.addRow(self.introduction)
        form.addRow('Working Time', self.worktime)
        form.addRow('Resting Time', self.resttime)
        form.addRow(self.ok_btn, self.cancel_btn)


    def unlock(self, text):
        # TODO: add another method check for both worktime and resttime
        if text:
            self.ok_btn.setEnabled(True)
        else:
            self.ok_btn.setDisabled(True)


    def ok_pressed(self):
        values = {'Date': self.date.date(),
                  'File': self.file_name.text(),
                  'Printer': self.printer_name.text()}
        self.accepted.emit(values)
        self.accept()


    def init_windows(self):
        """
        This method set the windows of the app
        and put it in the center of the screen
        """
        self.resize(400, 350)
        self.center()

        self.setWindowTitle('Help Information')
        self.show()

    
    def center(self):
        """
        This method centers the window on the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():
    app = QApplication(sys.argv)
    settng = PomodoroSettingGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
