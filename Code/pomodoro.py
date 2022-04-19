import math
from timer import Timer

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMessageBox


class Pomodoro(Timer):
    """
    The class Pomodoro creates a reminder and sends it to the user
    according to the Pomodoro choice of the user.

    The Pomodoro will work as a seperate timer of the app and will automatically run
    along with the program.

    NOTE: in the pop up windows for creating a Pomodoro, add the note of briefly explaining
    about Pomodoro technique, and then suggest default time is 25min worktime - 5min resttime
    """
    def __init__(self, worktime, resttime, countFrom=0):
        super().__init__(countFrom)
        self._start += countFrom

        self._worktime = worktime * 60
        self._resttime = resttime * 60
        self._cycle = 0 # one work + one rest = 2 cycle
        self._working = True
        self.start()

        """
        # Set a timer to call the update function periodically
        # TODO: Create some function to update the object every second
        self.timer = Timer()
        self.timer.timeout.connect(self.updateAll)
        self.timer.start(1000) # Update the time on the screen after every second

        # TODO: Create a input-getter in GUI to get worktime and resttime value for pomodoro
        """

    @property
    def worktime(self):
        return self._worktime

    @property
    def resttime(self):
        return self._resttime

    @property
    def cycle(self):
        return self._cycle

    @property
    def working(self):
        return self._working

    def get_rest(self):
        """
        This method checks if users have worked for worktime s, then create a notification for resting
        """
        if self.working:
            if math.isclose(self.duration, self.worktime, rel_tol=1):
                self.cycle += 1
                self.working = False
                
                rest_noti = QMessageBox()
                rest_noti.setIcon(QMessageBox.Warning)
                rest_noti.setWindowTitle("Have a Rest Notification")
                rest_noti.setText("You have been focused and working for {:d} minutes. It's time to have a {:d}-minute break. Try to relax and rest as much as possible. See you in {:d} minutes.".format(self.worktime//60, self.resttime//60, self.resttime//60))
                rest_noti.exec()

                self.restart()

    def get_work(self):
        """
        This method checks if users have rested for resttime s, then create a notification for working

        TODO: Check cycle to add long break after 4 pomodoro cycle
        """
        if not self.working:
            if math.isclose(self.duration, self.resttime, rel_tol=1):
                self.cycle += 1
                self.working = True
                
                work_noti = QMessageBox()
                work_noti.setIcon(QMessageBox.Warning)
                work_noti.setWindowTitle("Back to Work Notification")
                work_noti.setText("{:d}-minute break is over. It's time to get back to work!".format(self.resttime//60))
                work_noti.exec()

                self.restart()

    def update_pomodoro(self):
        self.get_rest()
        self.get_work()


pomodoro = Pomodoro(0.1, 0.1)

    

    