from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QPushButton,
                             QLabel, QVBoxLayout,
                             QHBoxLayout, QDesktopWidget)
from PyQt5.QtCore import QDate, Qt, pyqtSignal


class ChooseDaySettingGUI(QWidget):
    """
    The class ChooseDaySettingGUI creates a widget that contains a calendar that asks for the date that user would like to choose.
    
    The widget will pop up for the user to choose and then sends the information back to the backend.
    """
    accepted = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.init_windows()
        self.init_UI()

    def init_UI(self):
        """
        This method creates a layout and add the widgets to the pop up window widget
        
        The layout will have:
            - A calendar widget so that the user can choose day
            - A qlabel to show the date that user will choose
            - Buttons: """
        layout = QVBoxLayout(self)

        # calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.showDate)
        layout.addWidget(self.calendar)

        # QLabel to show date
        self.date_show = QLabel(self)
        self.date_show.setAlignment(Qt.AlignCenter)
        self.date = self.calendar.selectedDate()
        self.date_show.setText("You will open activities timer on " + self.date.toString())
        layout.addWidget(self.date_show)

        # Button layout with 2 buttons: OK + Cancel
        self.button_layout = QHBoxLayout()

        self.ok_btn = QPushButton('OK')
        self.ok_btn.clicked.connect(self.ok_pressed)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.button_layout.addWidget(self.ok_btn)
        self.button_layout.addWidget(self.cancel_btn)

        layout.addLayout(self.button_layout)

        self.setLayout(layout)


    def showDate(self, date):
        """
        This method shows the date that user choose
        """
        self.date_show.setText("You will open activities timer on " + date.toString())
        self.date = date

    
    def ok_pressed(self):
        """
        This method executes the window and sends the date user chose when the OK button is pressed
        """
        final_date = {"day": self.date.day(),
                    "month": self.date.month(),
                    "year": self.date.year()}
        self.accepted.emit(final_date)
        self.close()
        

    def init_windows(self):
        """
        This method set the windows of the app
        and put it in the center of the screen
        """
        self.resize(400, 400)
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
THE LINES BELOW ARE FOR TESTING THIS GUI

class Template(QWidget):

    def __init__(self):
        super().__init__()
        dg = ChooseDaySettingGUI()
        dg.accepted.connect(self.do_something)

        vbox = QVBoxLayout()
        vbox.addWidget(dg)

        self.setLayout(vbox)
        self.show()

    def do_something(self, values):
        print(values)


app = QApplication(sys.argv)
gui = Template()
sys.exit(app.exec())


def main():
    app = QApplication(sys.argv)
    ex = ChooseDaySettingGUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""

