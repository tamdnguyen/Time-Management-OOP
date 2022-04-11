import csv
from time_statistics import TimeStatistics


class DayTask():
    """
    The class AllTask represents the "brain" of the program. The information displayed on the GUI can be access from this class.
     
    The class works as a container and will store all the tasks inputted from the user.

    Main task of the class is to keep track of the amount of tasks added by the user and make sure that at most 5 tasks can be added simutaneously.

    The export functionality can also be implemented here (only export, print the data of that date)

    Read the documentation of Activity and Timer
    """

    # constant MAX represents the maximum amount of activities that can be added
    MAX = 5

    def __init__(self, date):
        """
        Creates a day, which will act like a container that includes all the tasks in that day

        @parameter:
            - date: the date will be inputted by the user (can create a calendar widget for the user to choose the date)
        """
        self._activities = []
        self._date = date
        self._statistics = TimeStatistics(self.data_for_time_statistic())

    def get_activities(self):
        """
        Return the activities list in that day
        """
        return self._activities

    def get_date(self):
        """
        Return the date of that day
        """
        return self._date

    def get_statistics(self):
        return self._statistics

    def add_activities(self, activity):
        """
        Adds the input activity to the activities list. Maximum 5 activities can be added
        
        @parameter:
            - activity: the activity to be added to the activities list
        
        Return:
            - True if added successfully
            - False if the activity can't be added
        """
        if activity.set_dayTask(self):
            self.get_activities().append(activity)
            return True
        else:
            return False

    def delete_activities(self, activity):
        """
        Delete the input activity from the activities list.
        
        @parameter:
            - activity: the activity to be deleted
        
        Return:
            - True if in the list and deleted successfully
            - False if not in the list"""

        if activity in self.get_activities():
            self.get_activities().remove(activity)
            return True
        else:
            return False

    def data_for_time_statistic(self):
        """
        Return the list of tasks in the dictionary form
        
        @return:
            dictionary with key-value is task_name-task_timer
        """
        day_data = {}
        activities_list = self.get_activities()
        for activity in activities_list:
            name = activity.get_name()
            time = activity.get_timer()

            day_data[name] = time
        
        return day_data
    
    def export_data(self):
        """
        This method creates a CSV file of the time management data of class DayTask
        """
        csv_message = ["NOTE: Exported file is in CSV type and is best viewed with Excel. For visualizing data", " please use Stats button in the app instead."]
        csv_header = ["Activity", "Time (in second)"]
        date = self.get_date()
        file_path = "time-management-oop/Code/time_data/" + str(date) + ".csv"

        with open(file_path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_message)
            writer.writerow(csv_header)
            for key, value in self.data_for_time_statistic().items():
                writer.writerow([key, value])
