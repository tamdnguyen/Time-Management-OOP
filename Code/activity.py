from timer import Timer
from date import Date
from time_conversion import TimeConversion


class Activity:
    """
    The class Activity represents the activities created by the users

    An activity has the information:
        - Activity name
        - The time counted of the activity
        - The date of the activity

    See the documentation of Timer, DayTask
    """
    def __init__(self, name=None, date=None):
        """
        Create a new activity with a given name from the user.
        
        @parameter: 
            - name (string): name of the activity
            @important
            - date (date object): the get_date() method of instance of class Day
                e.g., in main, create an instance A of class Day, then create an instance B
                of class Activity. The "date" parameter of instance B will be A.get_date()
                A = Day("04.04.2022")
                B = Activity("y2 project", A.get_date())
        """
        self.set_name(name)
        self._timer = Timer()
        self.set_date(date)

    def set_name(self, name):
        """
        Sets the name of the activity.
        If the given name is None or an empty
        string, the name is set to "Unknown activity".

        @parameter:
            - name (string): name of the activity
        """
        if name == None or name == "":
            self._name = "Unknown activity"
        else:
            self._name = name

    def set_date(self, date):
        """
        Sets the date of the activity.
        If the given date is None, the date is set to Today

        @parameter:
            - date (date object)
        """
        if date == None or date == "":
            self._date = Date.today()
        else:
            self._date = date

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
        @parameter 
            - format: integer [1,2,3,4]
                format: 1 => hour_min_sec
                        2 => min_sec
                        3 => fin_ect
                        4 => standard timedelta format
        Return a string with the desired format
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

    def edit_name(self, new_name):
        """
        Edit the name of the task

        @parameter:
            - new_name (string): inputted by the user
        """
        self._name = new_name
        
    def __str__(self):
        return "{:10s}{}\n{:10s}{}\n{:10s}{}".format("Activity:", self.get_name(), 
                                                     "Timer:", self.get_timer(), 
                                                     "Date:", self.get_date())
