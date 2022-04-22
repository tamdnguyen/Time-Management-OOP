import PyQt5
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QVBoxLayout, QHBoxLayout)
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_windows()
        self.init_UI()

        

    def init_UI(self):
        self.layout = QVBoxLayout()

        self.graphWidget = pg.PlotWidget()
        self.layout.addWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)

        self.setLayout(self.layout)

    
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


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()