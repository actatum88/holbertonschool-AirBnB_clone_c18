#!/usr/bin/python3
"""Amenity Unittest"""

import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """unittest"""

    def test_attrs(self):
        """unittest"""
        amenity1 = Amenity()
        self.assertEqual(amenity1.name, "")
        self.assertEqual(Amenity.name, "")
        self.assertIn("id", amenity1.__dict__)
        self.assertIn("created_at", amenity1.to_dict())
        self.assertIn("updated_at", amenity1.to_dict())

    def test_set(self):
        """unittest"""
        amenity2 = Amenity()
        amenity2.name = "Free WiFi"
        self.assertEqual(amenity2.name, "Free WiFi")

    def test_inheritance(self):
        """unittest"""
        amenity3 = Amenity()
        self.assertIsInstance(amenity3, BaseModel)
        self.assertIsInstance(amenity3, Amenity)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity4 = Amenity()
        hbnb_dict = amenity4.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "Amenity")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         amenity4.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         amenity4.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
