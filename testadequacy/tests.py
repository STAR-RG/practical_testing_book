#tests.py
from math import pi
import unittest
from area import *

class TestCircleArea(unittest.TestCase): 
    def test_area(self):
        #Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)