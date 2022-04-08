"""
Adding paths for the Code folder
"""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir_code = os.path.dirname(currentdir)
sys.path.append(parentdir_code)

import unittest
from time_statistics import TimeStatistics


class TestTimeStatistics(unittest.TestCase):
    """
    This class tests the methods in the class TimeStatistics
    
    First, Create a test data
    
    Format of test data:
        a dictionary with key-value for data of time management
        of a day (in the form of task_name-task_timer)
        Note: the value of the dictionary is the time in seconds
        
    E.g., Calculus 1: 7200, which means that the timer for task
    Calculus 1 is 7200 seconds, which is 2 hours
    """
    test_data = {"Calculus 1": 7200,
                "Linear Algebra": 7100.5,
                "Machine Learning": 7172.73,
                "Finnish 1": 1850.2,
                "Finland Work": 1850.2,
                "Aplus Manual": 17075.178,
                "Programming Y2": 18000,
                "Database": 18000}

    def setUp(self):
        self.statistics = TimeStatistics(TestTimeStatistics.test_data)

    def test_sum(self):
        time_sum = 7200 + 7100.5 + 7172.73 + 1850.2 + 1850.2 + 17075.178 + 18000 + 18000
        self.assertEqual(self.statistics.sum(), time_sum)

    def test_max(self):
        max_time = ["Programming Y2", "Database"]
        self.assertListEqual(self.statistics.max(), max_time)

    def test_min(self):
        min_time = ["Finnish 1", "Finland Work"]
        self.assertListEqual(self.statistics.min(), min_time)

    def test_time_range(self):
        range_time = [1850.2, 18000]
        self.assertListEqual(self.statistics.time_range(), range_time)
    
    def test_median(self):
        median_time = 7186.365
        self.assertAlmostEqual(self.statistics.median(), median_time)
    

if __name__ == "__main__":
    unittest.main()
