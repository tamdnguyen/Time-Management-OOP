import sys
from time import sleep
from gui import GUI
from PyQt5.QtWidgets import QApplication
from day_task import DayTask
from date import Date
from all_task import AllTask


def main():
    allTask = AllTask()
    allTask.import_file("Code/time_data/all_data.csv")

    today_day_task = allTask.add_days(DayTask(Date.today()))

    app = QApplication(sys.argv)
    gui = GUI(today_day_task)
    sys.exit(app.exec_())
    


if __name__ == '__main__':
    main()