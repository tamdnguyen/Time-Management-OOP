from timer import Timer
from datetime import date
from date import Date
from time_conversion import TimeConversion


class Activity:
    """
    The class Activity represents the activities created by the users

    An activity has the information:
        - Activity name
        - The time counted of the activity
        - The date of the activity

    See the documentation of Timer
    """
    def __init__(self, name):
        """
        Create a new activity with a given name from the user.
        The newly created activity initially has timer=0 and the date of creation
        
        @parameter: 
            - name (string): name of the activity
        """
        self.set_name(name)
        self._timer = Timer()
        self._date = Date.today()

    def set_name(self, name):
        """
        Sets the name of the activity.
        If the given name is None or an empty
        string, the name is set to "Unknown activity".

        @parameter:
            - name (string): name of the activity
        """
        if not name:
            self._name = "Unknown activity"
        else:
            self._name = name

    def get_name(self):
        """
        Return the activity name: string
        """
        return self._name

    def get_timer(self):
        """
        Return the activity timer
        """
        return self._timer

    def get_date(self):
        """
        Return the activity date
        """
        return self._date

    def set_time_format(self, format):
        """
        This method use TimeConversion class method to get the time format
        :param format: integer [1,2,3,4]
                format: 1 => hour_min_sec
                        2 => min_sec
                        3 => fin_ect
                        4 => standard timedelta format
        :return: a string with the desired format
        """
        time_conversion = TimeConversion(self.get_timer().duration)
        if format == 1:
            return time_conversion.hour_min_sec()
        elif format == 2:
            return time_conversion.min_sec()
        elif format == 3:
            return time_conversion.fin_etc()
        elif format == 4:
            return time_conversion.std_time()
        else:
            raise KeyError("Wrong key for activity time format")

    def __str__(self):
        return "{:10s}{}\n{:10s}{}\n{:10s}{}".format("Activity:", self.get_name(), 
                                                     "Timer:", self.get_timer(), 
                                                     "Date:", self.get_date())
