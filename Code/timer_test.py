from activity import Activity
import time
from timer2 import Timer2


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
    timer = Timer2()
    timer2 = Timer2(5)
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

test_timer2()
