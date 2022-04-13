# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from timer import Timer
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Stop watch")
        self.setGeometry(100, 100, 400, 500)
        self.UiComponents()
        self.show()
  
    # method for widgets
    def UiComponents(self):
        # creating real timer for activity
        self.stopwatch = Timer()
  
        # creating flag
        self.flag = False
        self.label = QLabel(self)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet("border : 4px solid black;")
        self.label.setText("{:d}".format(round(self.stopwatch.duration)))
        self.label.setFont(QFont('Arial', 25))
        self.label.setAlignment(Qt.AlignCenter)

        start = QPushButton("Start", self)
        start.setGeometry(125, 250, 150, 40)
        start.pressed.connect(self.Start)
  
        # creating pause button
        pause = QPushButton("Pause", self)
        pause.setGeometry(125, 300, 150, 40)
        pause.pressed.connect(self.Pause)
  
        # creating reset button
        re_set = QPushButton("Reset", self)
        re_set.setGeometry(125, 350, 150, 40)
        re_set.pressed.connect(self.Reset)
  
        # creating a timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # miliseconds
  
    # method called by timer
    def showTime(self):
        self.label.setText("{:d}".format(round(self.stopwatch.duration)))
  
    def Start(self):
        self.stopwatch.start()
  
    def Pause(self):
        self.stopwatch.stop()
  
    def Reset(self):
        self.stopwatch.reset()
        self.label.setText("{:d}".format(round(self.stopwatch.duration)))
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())