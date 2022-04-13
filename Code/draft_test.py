from activity import Activity
import time
from timer import Timer
from day_task import DayTask
from all_task import AllTask
from date_generator import DateGenerator


def main():
    name = str(input("Enter task name\n"))
    task = Activity(name)
    print(task)

    time.sleep(10)
    print(task)

    task.get_timer().stop()
    print(task)
    time.sleep(5)
    print(task)

    task.get_timer().start()
    time.sleep(70)
    print(task)
    print(task.set_time_format(1))


def test_timer2():
    timer = Timer()
    timer2 = Timer(5)
    timer.start()
    timer2.start()

    print(timer)
    print(timer2)

    time.sleep(10)
    print(timer)
    print(timer2)

    timer.stop()
    timer2.stop()
    print(timer)
    print(timer2)

    time.sleep(5)
    print(timer)
    print(timer2)

    timer.start()
    timer2.start()
    time.sleep(15)
    print(timer)
    print(timer2)


def test_import_date():
    filename = "13-04-2022.csv"
    file_path = "time-management-oop/Code/time_data/" + filename

    dayTask = DayTask(DateGenerator(filename[:-4]))

    print(dayTask)

    dayTask.import_date(file_path)
    print(dayTask.get_activities())

    for activity in dayTask.get_activities():
        print(activity)

def test_import_file():
    file_path = "time-management-oop/Code/time_data/all_data.csv"

    allTask = AllTask()
    
    allTask.import_file(file_path)
    print(allTask.get_days())

    for dayTask in allTask.get_days():
        print(dayTask)
        print(dayTask.get_activities())
        for activity in dayTask.get_activities():
            print(activity)

test_import_date()
test_import_file()