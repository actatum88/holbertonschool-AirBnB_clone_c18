#!/usr/bin/python3
"""This module tests the Place class"""


import unittest
from models.state import State


class TestPlace(unittest.TestCase):
    """Testing the State Class"""

    def setUp(self):
        """Setup before each method"""
        self.a = State()

    def tearDown(self):
        """Cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """test initilization"""
        self.assertEqual(self.a.name, "")
        aDict = self.a.to_dict()
        b = Place(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)