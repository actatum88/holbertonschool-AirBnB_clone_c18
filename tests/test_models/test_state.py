#!/usr/bin/python3
"""State Unittest"""

import unittest
import pep8
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """unittest"""

    def test_attrs(self):
        """unittest"""
        state1 = State()
        self.assertEqual(state1.name, "")
        self.assertEqual(State.name, "")
        self.assertIn("id", state1.__dict__)
        self.assertIn("created_at", state1.to_dict())
        self.assertIn("updated_at", state1.to_dict())

    def test_set(self):
        """unittest"""
        state2 = State()
        state2.name = "Oklahoma"
        self.assertEqual(state2.name, "Oklahoma")

    def test_inheritance(self):
        """unittest"""
        state3 = State()
        self.assertIsInstance(state3, BaseModel)
        self.assertIsInstance(state3, State)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        state4 = State()
        hbnb_dict = state4.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "State")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         state4.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         state4.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
