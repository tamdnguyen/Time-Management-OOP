import sys
from time import sleep
from gui import GUI
from PyQt5.QtWidgets import QApplication
from day_task import DayTask
from datetime import date
from activity import Activity
from date import Date
from all_task import AllTask
from date_generator import DateGenerator


def main():
    """
    TODO: Write the official main
    """
    allTask = AllTask()

    today_day_task = DayTask(Date.today())

    activity_1 = Activity("activity_1", 10.9098)
    activity_2 = Activity("activity_2", 1)
    activity_3 = Activity("activity_3", 1)

    today_day_task.add_activities(activity_1)
    today_day_task.add_activities(activity_2)
    today_day_task.add_activities(activity_3)

    tomorrow_day_task = DayTask(DateGenerator("14-04-2022.csv"[:-4]).create_date())
    activity_4 = Activity("activity_4", 10.09203)
    activity_5 = Activity("activity_5", 100)
    activity_6 = Activity("activity_6")

    tomorrow_day_task.add_activities(activity_4)
    tomorrow_day_task.add_activities(activity_5)
    tomorrow_day_task.add_activities(activity_6)


    print(activity_3)
    print(activity_5)
    activity_3.get_timer().start()
    activity_5.get_timer().start()
    activity_4.get_timer().start()
    activity_6.get_timer().start()

    allTask.add_days(today_day_task)
    allTask.add_days(tomorrow_day_task)

    app = QApplication(sys.argv)
    gui = GUI(tomorrow_day_task)
    sys.exit(app.exec_())
    


if __name__ == '__main__':
    main()