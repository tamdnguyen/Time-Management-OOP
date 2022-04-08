"""
!IMPORTANT

Implement the Pie chart, Bar Chart as the extensions of statistics
"""


# importing pyqtgraph as pg
import pyqtgraph as pg
  
# importing QtCore and QtGui from 
# the pyqtgraph module
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5 import QtWidgets
  
# importing numpy as np
import numpy as np
  
import time
  
# creating a pyqtgraph plot window
window = pg.plot()
  
# setting window geometry
# left = 100, top = 100
# width = 600, height = 500
window.setGeometry(100, 100, 600, 500)
  
# title for the plot window
title = "GeeksforGeeks PyQtGraph"
  
# setting window title to plot window
window.setWindowTitle(title)
  
# create list for y-axis
y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
  
# create horizontal list i.e x-axis
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
# create pyqt5graph bar graph item
# with width = 0.6
# with bar colors = green
bargraph = pg.BarGraphItem(x = x, height = y1, width = 0.6, brush ='g')
  
# add item to plot window
# adding bargraph item to the window
window.addItem(bargraph)
  
  
# main method
if __name__ == '__main__':
      
    # importing system
    import sys
      
    # Start Qt event loop unless running in interactive mode or using
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()