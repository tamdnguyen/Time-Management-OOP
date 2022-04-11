import sys
from time import sleep
from gui import GUI
from PyQt5.QtWidgets import QApplication
from day_task import DayTask
from datetime import date
from activity import Activity
from date import Date

def main():

    today_day_task = DayTask(Date.today())

    activity_1 = Activity("activity_1", 10.9098)
    activity_2 = Activity("activity_2", 1)
    activity_3 = Activity("activity_3", 1)

    today_day_task.add_activities(activity_1)
    today_day_task.add_activities(activity_2)
    today_day_task.add_activities(activity_3)

    print(activity_3)
    activity_3.get_timer().start()
    sleep(5)
    print(activity_3) 

    today_day_task.export_data()

    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()