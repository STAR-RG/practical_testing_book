# Hands on: Unit Testing with Python

from IPython.display import YouTubeVideo

YouTubeVideo('1Lfv5tUGsn8')

# Vamos definir a classe circle em python

from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius must not be negative.")
    return pi*(r**2) 

# Agora vamos escrever testes de unidade para esta classe

import unittest

class TestCircleArea(unittest.TestCase): 
    def test_area(self):
        #Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        #Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        #Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "text")

