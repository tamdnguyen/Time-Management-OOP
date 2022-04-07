from datetime import timedelta


class TimeConversion:
    """
    These constants represent the time conversion
    equivalent to time in seconds
    """

    MINUTE = 60
    HOUR = 60 * MINUTE
    FIN_ECTS = 27 * HOUR

    def __init__(self, time):
        self._time = time

    @property
    def time(self):
        return self._time

    def hour_min_sec(self):
        """
        Return the time format in form of HH:MM:SS
        e.g., 5 hours, 40 minutes and 20 seconds => 05:40:20
        """
        time = ""
        hour = round(self.time // self.HOUR)
        min = round((self.time - self.HOUR * hour) // self.MINUTE)
        sec = round(self.time - self.HOUR * hour - self.MINUTE * min)

        if hour < 10:
            time += "0" + str(hour)
        else:
            time += str(hour)
        time += ":"

        if min < 10:
            time += "0" + str(min)
        else:
            time += str(min)
        time += ":"

        if sec < 10:
            time += "0" + str(sec)
        else:
            time += str(sec)

        return time

    def min_sec(self):
        """
        Return the time format in form of MM:SS
        e.g., 5 hours, 40 minutes and 20 seconds => 340:20
        """
        time = ""
        min = round(self.time // self.MINUTE)
        sec = round(self.time - self.MINUTE * min)

        if min < 10:
            time += "0" + str(min)
        else:
            time += str(min)
        time += ":"

        if sec < 10:
            time += "0" + str(sec)
        else:
            time += str(sec)

        return time

    def fin_etc(self):
        """
        Return the time in format number of credits according to Finland ECTS
        e.g, 27h = 1 credit
                100000 sec = 1,029 cre
        """
        ect = self.time // self.FIN_ECTS
        return "{:.3f} ECTS".format(ect)

    def std_time(self):
        """
        Return the time in standard format of timedelta
        """
        sec = round(self.time)
        return str(timedelta(seconds=sec))
