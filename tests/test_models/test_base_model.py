#!/usr/bin/python3
"""Tests the Base Model."""

import unittest
from models.base_model import BaseModel
import datetime
import json


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel Class"""

from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        
    def test_pep8_conformance(self):
        """test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base_model.py', 'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
