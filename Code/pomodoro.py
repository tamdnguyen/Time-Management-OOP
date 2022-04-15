import math
from timer import Timer


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
        self._worktime = worktime
        self._resttime = resttime
        self._cycle = 0
        self._working = True
        self.start()

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
        if self.working:
            if math.isclose(self.duration, self.worktime, rel_tol=1):
                self.reset()
                self.working = False
                return "Have a rest now"

    def get_work(self):
        if not self.working:
            if math.isclose(self.duration, self.resttime, rel_tol=1):
                self.reset()
                self.reset()
                return "It's time to get back to work"

    

    

    