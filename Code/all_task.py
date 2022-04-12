import csv
from day_task import DayTask
from activity import Activity

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
        Add the days to the container if the date of the DayTask object has not existed in the list
        """
        if day.set_allTask(self):
            self._days.append(day)

    def existed(self, day):
        """
        Check if the created day is already in the DayTask or not
        (if yes, then it means that the day has been created before, so we will
        continue our program with the data of that day instead of creating a new day)

        We check is by comparing the date of 2 the DayTask object "day" vs the DayTasks object
        in the list of the class AllTask
        
        Return
            - False, day if the day has not been created so we will create a new DayTask object day
            - True, DayTask object existed in the list of AllTask before"""
        for dayTask in self.get_days():
            if dayTask.get_date() == day.get_date():
                return True, dayTask
        
        return False, day

    def export_file(self):
        """
        This method creates CSV file named "all_data.csv" which acts as a central database of the program and has all the information about AllTask, DayTask, Activity
        """
        csv_message = ["NOTE: Exported file is in CSV type and is best viewed with Excel. For visualizing data", " please use Stats button in the app instead."]
        csv_header = ["Date", "Activity", "Time (in second)"]
        file_path = "time-management-oop/Code/time_data/all_data.csv"

        with open(file_path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_message)
            writer.writerow(csv_header)
            for dayTask in self.get_days():
                for key, value in dayTask.data_for_time_statistic().items():
                    writer.writerow([dayTask.get_date(), key, value])

    def import_file(self, filename):
        """
        This method reads a CSV file named "all_data.csv" and creates the DayTask, Activity objects for the program
        
        TODO: add the exceptions and raise errors to deal with problems while reading files
        """
        try:
            file = open(filename, "r")
            linelist = file.readlines()
            file.close()

            allTask = AllTask()

            for line in linelist[2:]:
                line = line.strip()
                parts = line.split(",")

                # TODO: run main to see if it is possible to create DayTask with string value like this
                dayTask = DayTask(parts[0])
                activity = Activity(parts[1], parts[2])
                dayTask.add_activities(activity)
                allTask.add_days(dayTask)
        except OSError:
            print("Invalid file")
            return 0
    

            


        

