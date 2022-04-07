class AllTask():
    """
    The class AllTask represents the "world" of the program.
     
    The class works as a container and will store all the days from the DayTask.

    Main task of the class is to store and manage the files as a whole.

    The function move_to_next_day() can possibly be implemented in this class. The function can be for example: save the day to a file, create the next day in the "days world".

    Read the documentation of DayTask, Activity and Timer
    """
    def __init__(self):
        """
        Create the containers for all the days of the app (central database)
        """
        self._days = []

    def get_days(self):
        """
        Return the list of the days of the app
        """
        return self._days

    def add_days(self, day):
        """
        Add the days to the container
        """
        self._days.append(day)
    
