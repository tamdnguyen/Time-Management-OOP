from date import Date

class DateGenerator:
    """
    This class is a supplementary class for Date class.
    It reads in a string of some time expression, and then it
    extracts the day, month, year, and then returns the corresponding date.
    
    This class is helpful for method import_date() of class DayTask
    and method import_data() of class AllTask

    See the documentation of class DayTask, AllTask, and Date
    """
    def __init__(self, time_expression):
        self._time_expression = time_expression

    @property
    def time_expression(self):
        return self._time_expression

    def create_date(self):
        time_expression = str(self.time_expression)[0:-4]
        date_data  = time_expression.split("-")
        day = int(date_data[0])
        month = int(date_data[1])
        year = int(date_data[2])

        corresponding_date = Date(year, month, day)

        return corresponding_date