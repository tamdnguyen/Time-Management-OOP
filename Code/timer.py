import time


class Timer:
    """
    The class Timer represents a digital clock to count the time of the activity
    """
    def __init__(self, countFrom = 0):
        self._countFrom = float(countFrom)
        self._start = time.time() - self.countFrom
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
    def countFrom(self):
        """
        Return the countFrom value (from what value the timer counts)

        This countFrom value is for the reading/importing file. When reading/importing
        file, the timer will have some predefined value (e.g., the timer has counted 2 hours before, so we need to continue counting from that value)
        """
        return self._countFrom

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

