import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QMessageBox


class GUI(QWidget):
    """
    The class GUI create the graphical user interface of the program using PyQt5
    """
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        This method creates the initial GUI of the program
        """
        self.resize(1000, 1000)
        self.center()

        self.setWindowTitle('Time Management App')

        self.show()

    def closeEvent(self, event):
        """
        This method confirms if the user wants to quit or not
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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
    gui = GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()