#!/usr/bin/python3
"""This module tests the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing the User Class"""

    def setUp(self):
        """setup before each method"""
        self.a = User()

    def tearDown(self):
        """cleanup after each method"""
        pass
