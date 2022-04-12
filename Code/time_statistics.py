from time import time


class TimeStatistics:
    """
    The class TimeStatistics calculates the statistics from the
    time management data in a day.

    The statistics include:
        - summary statistics
            - total time (sum)
            - max
            - min
            - average time (mean)
            - range
            - median
        - graph & chart
            - equivalent percentages of the task time contribute to the whole day (into a table)
            - pie chart
            - bar chart

    Usage: TimeStatistics(DayTask_object.data_for_time_statistic())
    
    See the document of DayTask
    """
    def __init__(self, data):
        """
        @parameter:
            - data: a dictionary with key-value for data of time management
            of a day (in the form of task_name-task_timer)
        """
        self._data = data

    def get_data(self):
        """
        Return the data dictionary
        """
        return self._data

    def sum(self):
        """
        @return:
            - sum of the time of all tasks
        """
        return sum(list(self.get_data().values()))

    def max(self):
        """
        @return:
            - max_activity (list): the activity (activities) list that has max time
        """
        data = self.get_data()
        time_max = max(list(data.values()))
        max_activity = []
        
        for name, time in data.items():
            if time == time_max:
                max_activity.append(name)
        
        return max_activity
    
    def min(self):
        """
        @return:
            - min_activity (list): the activity (activities) list that has min time
        """
        data = self.get_data()
        time_min = min(list(data.values()))
        min_activity = []
        
        for name, time in data.items():
            if time == time_min:
                min_activity.append(name)
        
        return min_activity

    def time_range(self):
        """
        @return:
            - time_range (list): 2 elements list, min and max time
        """
        data = self.get_data()

        task_max = self.max()[0]
        time_max = data[task_max]

        task_min = self.min()[0]
        time_min = data[task_min]

        return [time_min, time_max]

    def median(self):
        """
        @return:
            - median (float): the value separating the higher half from the lower half of a data time management
        """
        data = self.get_data()
        time = list(data.values())

        time.sort()

        # find the median
        if len(time) % 2 != 0:
            # total number of values are odd
            # subtract 1 since indexing starts at 0
            m = int((len(time)+1)/2 - 1)
            return time[m]
        else:
            m1 = int(len(time)/2 - 1)
            m2 = int(len(time)/2)
            return (time[m1]+time[m2])/2
        