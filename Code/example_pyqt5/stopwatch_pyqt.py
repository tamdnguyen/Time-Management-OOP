# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Stop watch")
        self.setGeometry(100, 100, 400, 500)
        self.UiComponents()
        self.show()
  
    # method for widgets
    def UiComponents(self):
        self.count = 0
  
        # creating flag
        self.flag = False
        self.label = QLabel(self)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet("border : 4px solid black;")
        self.label.setText(str(self.count))
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
        re_set = QPushButton("Re-set", self)
        re_set.setGeometry(125, 350, 150, 40)
        re_set.pressed.connect(self.Re_set)
  
        # creating a timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
  
    # method called by timer
    def showTime(self):
        # checking if flag is true
        if self.flag:
            # incrementing the counter
            self.count+= 1
        # getting text from count
        text = str(self.count / 10)
        # showing text
        self.label.setText(text)
  
    def Start(self):
        # making flag to true
        self.flag = True
  
    def Pause(self):
        # making flag to False
        self.flag = False
  
    def Re_set(self):
        # making flag to false
        self.flag = False
  
        # reseeting the count
        self.count = 0
  
        # setting text to label
        self.label.setText(str(self.count))
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())