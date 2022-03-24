from timer import Timer
from datetime import date


class Activity:
    """
    The class Activity represents the activities created by the users

    An activity has the information:
        - Activity name
        - The time counted of the activity
        - The date of the activity

    See the documentation of Date and Timer
    """
    def __init__(self, name):
        """
        Create a new activity with a given name from the user.
        The newly created activity initially has timer=0 and the date of creation
        
        @parameter: 
            - name (string): name of the activity
            - date (object Date()): the date of the activity
        """
        self.set_name(name)
        self._timer = Timer()
        self._date = date.today()

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

    def __str__(self):
        return "{:10s}{}\n{:10s}{}\n{:10s}{}".format("Activity:", self.get_name(), 
                                                     "Timer:", self.get_timer(), 
                                                     "Date:", self.get_date())
