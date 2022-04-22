from operator import le
import PyQt5
from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QVBoxLayout, QHBoxLayout,
                            QTableWidget, QTableWidgetItem)
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from time_statistics import TimeStatistics


class StatisticsGUI(QWidget):
    """
    The class StatisticsGUI creates a widgets that shows the statistics and visualization of time management data of the GUI app.
    """

    def __init__(self, dayTask):
        super().__init__()

        self.dayTask = dayTask
        self.data_raw = self.dayTask.data_for_time_statistic()
        self.data_percentage = self.get_data_percentage()

        self.statistics = TimeStatistics(self.data_raw)

        self.init_windows()
        self.init_UI()


    def init_UI(self):
        """
        This method creates a layout and add the widgets to the pop up window widget
        
        The layout will have:
            - Statistics table: 2 vertical tables side by side. The left table is for the activities timer information. The right table is for statistics overview.
            - Pie chart
            - Bar chart
        """
        self.layout = QVBoxLayout()

        # create the layout for the tables
        self.table_layout = QHBoxLayout()
        self.table_layout_func()

        self.graphWidget = pg.PlotWidget()

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)

        # add the widgets to the layout
        self.layout.addLayout(self.table_layout)
        self.layout.addWidget(self.graphWidget)

        self.setLayout(self.layout)


    def table_layout_func(self):
        """
        This method creates the table and the content of the table to show the activities timer information
        """

        # Left table: showing the timer and their contribution
        self.table_display_create()

        # Right table: showing the statistic overviews
        self.table_overview_create()

        # add the tables to the layout
        self.table_layout.addWidget(self.table_display)
        self.table_layout.addWidget(self.table_overview)

    
    def table_display_create(self):
        """
        This method creates the display table, which is the left table on the first row of the pop up widget
        
        See method table_layout_func() and init_UI()
        """
        # create the table
        self.table_display = QTableWidget()
        self.table_display.setRowCount(len(self.data_raw))
        self.table_display.setColumnCount(3)

        self.table_display.setHorizontalHeaderLabels(["Activity", "Timer (s)", "Contribution (%)"])

        # add the content for the table
        for i in range(len(self.data_raw)):
            activity = list(self.data_raw.keys())[i]
            timer_raw = list(self.data_raw.values())[i]
            timer_percentage = list(self.data_percentage.values())[i]

            self.table_display.setItem(i, 0, QTableWidgetItem("{:s}".format(activity)))
            self.table_display.setItem(i, 1, QTableWidgetItem("{:.2f}".format(timer_raw)))
            self.table_display.setItem(i, 2, QTableWidgetItem("{:.2f}".format(timer_percentage)))

        # Resize of the rows and columns based on the content
        self.table_display.resizeColumnsToContents()
        self.table_display.resizeRowsToContents()

        # make the table view-only
        self.table_display.setEditTriggers(QTableWidget.NoEditTriggers)
    

    def table_overview_create(self):
        """
        This method creates the overview table, which is the right table on the first row of the pop up widget
        
        See method table_layout_func() and init_UI()
        """
        # create the table
        self.table_overview = QTableWidget()
        self.table_overview.setRowCount(5)
        self.table_overview.setColumnCount(2)

        self.table_overview.setHorizontalHeaderLabels(["Descriptive Statistics", "Value (s)"])

        # add the content for the table
        self.table_overview.setItem(0, 0, QTableWidgetItem("Total Time"))
        self.table_overview.setItem(0, 1, QTableWidgetItem("{:.2f}".format(self.statistics.sum())))
        self.table_overview.setItem(1, 0, QTableWidgetItem("Max Time"))
        self.table_overview.setItem(1, 1, QTableWidgetItem("{:.2f}".format(self.statistics.max())))
        self.table_overview.setItem(2, 0, QTableWidgetItem("Min Time"))
        self.table_overview.setItem(2, 1, QTableWidgetItem("{:.2f}".format(self.statistics.min())))
        self.table_overview.setItem(3, 0, QTableWidgetItem("Range"))
        self.table_overview.setItem(3, 1, QTableWidgetItem("{:.2f}".format(self.statistics.time_range())))
        self.table_overview.setItem(4, 0, QTableWidgetItem("Median Time"))
        self.table_overview.setItem(4, 1, QTableWidgetItem("{:.2f}".format(self.statistics.median())))

        # Resize of the rows and columns based on the content
        self.table_overview.resizeColumnsToContents()
        self.table_overview.resizeRowsToContents()

        # make the table view-only
        self.table_overview.setEditTriggers(QTableWidget.NoEditTriggers)


    def init_windows(self):
        """
        This method set the windows of the app
        and put it in the center of the screen

        TODO: check when the activities list is empty and deal with that
        """
        # check if the data is empty then close the windows immediately
        print(self.data_percentage)

        if self.data_percentage is None:
            print("is None")
            self.close()
            print("not close")

        self.resize(400, 400)
        self.center()

        self.setWindowTitle('Statistics Visualization')

    
    def center(self):
        """
        This method centers the window on the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def get_data_percentage(self):
        """
        This method creates a new dictionary with the key being activities name and values being their timer percentage of contributing to the whole dayTask timer sum
        """
        data_percentage = {}

        data = self.data_raw
        timer_sum = sum(data.values())

        try:
            for activity in list(data.keys())[:-1]:
                data_percentage[activity] = round((data[activity]/timer_sum)*100, 2)

            # for the last activity timer, we use 100-(sum of percentage of other activities)
            sum_so_far = sum(data_percentage.values())
            last_activity = list(data.keys())[-1]

            data_percentage[last_activity] = 100 - sum_so_far
        except IndexError:
            return None

        return data_percentage

"""
def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""
