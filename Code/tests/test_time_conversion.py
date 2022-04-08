"""
Adding paths for the Code folder
"""
import os, sys
from sqlite3 import Time
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir_code = os.path.dirname(currentdir)
sys.path.append(parentdir_code)

import unittest
from time_conversion import TimeConversion


class TestTimeConversion(unittest.TestCase):
    """
    This class tests the methods in the class TimeConversion
    
    First, Create a test data
    
    Format of test data:
        a float value of time in seconds
        e.g., 100000 or 171872913,120938

    In this class, the tests will not be test the TimeConversion class method by method
    Instead, there will be 6 test data, which are equivalent to 6 test cases

    For each test test case, the test data will be a little different, 
    and there will be different assertion to test all the methods in TimeConversion class
    """        

    def test_data_1(self):
        test_data = 1432 # 00:23:52
        model = TimeConversion(test_data)

        hour_min_sec = "00:23:52"
        min_sec = "23:52"
        fin_etc = "0.015 ECTS"

        self.assertEqual(model.hour_min_sec(), hour_min_sec)
        self.assertEqual(model.min_sec(), min_sec)
        self.assertEqual(model.fin_etc(), fin_etc)

    def test_data_2(self):
        test_data = 100000 # 27:46:40
        model = TimeConversion(test_data)

        hour_min_sec = "27:46:40"
        min_sec = "1666:40"
        fin_etc = "1.029 ECTS"

        self.assertEqual(model.hour_min_sec(), hour_min_sec)
        self.assertEqual(model.min_sec(), min_sec)
        self.assertEqual(model.fin_etc(), fin_etc)

    def test_data_3(self):
        test_data = 0 # 00:00:00
        model = TimeConversion(test_data)

        hour_min_sec = "00:00:00"
        min_sec = "00:00"
        fin_etc = "0.000 ECTS"

        self.assertEqual(model.hour_min_sec(), hour_min_sec)
        self.assertEqual(model.min_sec(), min_sec)
        self.assertEqual(model.fin_etc(), fin_etc)

    def test_data_4(self):
        test_data = 21599 # 05:59:59
        model = TimeConversion(test_data)

        hour_min_sec = "05:59:59"
        min_sec = "359:59"
        fin_etc = "0.222 ECTS"

        self.assertEqual(model.hour_min_sec(), hour_min_sec)
        self.assertEqual(model.min_sec(), min_sec)
        self.assertEqual(model.fin_etc(), fin_etc)

    def test_data_5(self):
        test_data = 56789.1234 # 15:46:29
        model = TimeConversion(test_data)

        hour_min_sec = "15:46:29"
        min_sec = "946:29"
        fin_etc = "0.584 ECTS"

        self.assertEqual(model.hour_min_sec(), hour_min_sec)
        self.assertEqual(model.min_sec(), min_sec)
        self.assertEqual(model.fin_etc(), fin_etc)

    def test_data_6(self):
        test_data = 12345.6789 # 03:25:46
        model = TimeConversion(test_data)

        hour_min_sec = "03:25:46"
        min_sec = "205:46"
        fin_etc = "0.127 ECTS"

        self.assertEqual(model.hour_min_sec(), hour_min_sec)
        self.assertEqual(model.min_sec(), min_sec)
        self.assertEqual(model.fin_etc(), fin_etc)


if __name__ == "__main__":
    unittest.main()
                                                                                                                                                                                                                                                                                 