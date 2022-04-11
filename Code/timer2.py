import time


class Timer2:
    """
    The class Timer represents a digital clock to count the time of the activity
    """
    def __init__(self, startingTime=0):
        self._statingTime = startingTime
        self._start = time.time() - self.startingTime
        self._end = None
        self.stop()

    @property
    def duration(self):
        """
        Return the duration of the task: time (unit: second)
        """
        if self._end is not None:
            return self._end - self._start
        else:
            return time.time() - self._start

    @property
    def running(self):
        """
        Return if the timer is running: boolean
        """
        return not self._end

    @property
    def startingTime(self):
        return self._statingTime

    def start(self):
        """
        This method starts/resumes the timer
        """
        if not self.running:
            self._start = time.time() - self.duration
            self._end = None

    def stop(self):
        """
        This method stops/pauses the timer
        """
        if self.running:
            self._end = time.time()

    def restart(self):
        """
        This method restart the timer

        After this method is called, the timer duration goes
        back to zero and starts itself automatically
        """
        self._start = time.time()
        self._end = None

    def reset(self):
        """
        This method reset the timer

        After this method is called, the timer duration goes back to zero and stops counting time. 
        To start the timer, .start() needs to be called
        """
        self._start = time.time()
        self._end = self._start

    def __str__(self):
        time = self.duration
        return "{:f}s".format(time)

