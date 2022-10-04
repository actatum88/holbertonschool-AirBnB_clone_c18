#!/usr/bin/python3
"""This module tests the City class"""


import unittest
from models.city import City


class TestAmenity(unittest.TestCase):
    """Testing the City Class"""

    # Setting up using ClassMethod to check __init__

    def setUp(self):
        """setup before each method"""
        self.a = City()

    def tearDown(self):
        """cleanup after each method"""
        pass
