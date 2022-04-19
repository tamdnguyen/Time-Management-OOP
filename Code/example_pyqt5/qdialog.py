import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel, QLineEdit, QDateEdit, QFormLayout, QWidget

from PyQt5.QtCore import QDate, pyqtSignal

class Dialog(QDialog):

    accepted = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date = QDateEdit()
        self.date.setDisplayFormat('MMM d, yyyy')
        self.date.setDate(QDate.currentDate())
        self.file_name = QLineEdit()
        self.file_name.textEdited[str].connect(self.unlock)
        self.printer_name = QLineEdit()
        self.btn = QPushButton('OK')
        self.btn.setDisabled(True)
        self.btn.clicked.connect(self.ok_pressed)

        form = QFormLayout(self)
        form.addRow('Date', self.date)
        form.addRow('*File Name', self.file_name)
        form.addRow('Printer Name', self.printer_name)
        form.addRow(self.btn)

    def unlock(self, text):
        if text:
            self.btn.setEnabled(True)
        else:
            self.btn.setDisabled(True)

    def ok_pressed(self):
        values = {'Date': self.date.date(),
                  'File': self.file_name.text(),
                  'Printer': self.printer_name.text()}
        self.accepted.emit(values)
        self.accept()

class Template(QWidget):

    def __init__(self):
        super().__init__()
        dg = Dialog()
        dg.accepted.connect(self.do_something)
        dg.exec_()

    def do_something(self, values):
        print(values['File'], values['Date'], values['Printer'])


app = QApplication(sys.argv)
gui = Template()
sys.exit(app.exec_())