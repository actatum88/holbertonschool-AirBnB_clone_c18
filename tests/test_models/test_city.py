#!/usr/bin/python3
"""City Unittest"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """unittest"""

    def test_attrs(self):
        """unittest"""
        city1 = City()
        self.assertEqual(city1.name, "")
        self.assertEqual(City.name, "")
        self.assertEqual(city1.state_id, "")
        self.assertEqual(City.state_id, "")
        self.assertIn("id", city1.__dict__)
        self.assertIn("created_at", city1.to_dict())
        self.assertIn("updated_at", city1.to_dict())

    def test_set(self):
        """unittest"""
        city2 = City()
        city2.name = "Tulsa"
        self.assertEqual(city2.name, "Tulsa")
        city2.state_id = "123"
        self.assertEqual(city2.state_id, "123")
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")

    def test_inheritance(self):
        """unittest"""
        city3 = City()
        self.assertIsInstance(city3, BaseModel)
        self.assertIsInstance(city3, City)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city4 = City()
        hbnb_dict = city4.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "City")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"], city4.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"], city4.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
