from activity import Activity
import time


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


main()
