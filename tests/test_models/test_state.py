#!/usr/bin/python3
"""This module tests the State class"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing the State Class"""

    def setUp(self):
        """setup before each method"""
        self.a = State()

    def tearDown(self):
        """cleanup after each method"""
        pass
