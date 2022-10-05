#!/usr/bin/python3
"""BaseModel Unittest"""

import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """unittest"""

    def test_init(self):
        """unittest"""
        base_model1 = BaseModel()
        base_model1.id = 12
        base_model1_dict = {
            "updated_at": "2022-10-31T23:12:48.287044",
            "created_at": "2022-10-31T23:12:48.287044",
            "id": "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9",
            "__class__": "BaseModel"
        }
        base_model1_kwargs = BaseModel(**base_model1_dict)
        self.assertEqual(base_model1.id, 12)
        self.assertIsInstance(base_model1, BaseModel)
        self.assertIsNotNone(base_model1.created_at)
        self.assertIsNotNone(base_model1.updated_at)
        self.assertIn("created_at", base_model1.__dict__)
        self.assertIn("updated_at", base_model1.__dict__)
        self.assertIn("id", base_model1.__dict__)
        self.assertIsInstance(base_model1.created_at, datetime)
        self.assertIsInstance(base_model1.updated_at, datetime)
        self.assertEqual(base_model1_kwargs.id,
                         "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9")
        self.assertIsInstance(base_model1_kwargs, BaseModel)
        self.assertIsNotNone(base_model1.created_at)
        self.assertIsNotNone(base_model1.updated_at)
        self.assertIn("created_at", base_model1_kwargs.__dict__)
        self.assertIn("updated_at", base_model1_kwargs.__dict__)
        self.assertIn("id", base_model1_kwargs.__dict__)
        self.assertIsInstance(base_model1_kwargs.created_at, datetime)
        self.assertIsInstance(base_model1_kwargs.updated_at, datetime)

    def test_str(self):
        """unittest"""
        base_model2 = BaseModel()
        base_model2_str = str(base_model2)
        base_model2_format = "[BaseModel] ({}) {}".format(
            base_model2.id, base_model2.__dict__)
        self.assertEqual(base_model2_str, base_model2_format)

    def test_dict(self):
        """unittest"""
        base_model3 = BaseModel()
        dict_test = base_model3.to_dict()
        self.assertIn('__class__', dict_test)
        self.assertIn("updated_at", dict_test)
        self.assertIn("created_at", dict_test)
        self.assertIn("id", dict_test)
        self.assertEqual(dict_test.get("updated_at"),
                         str(base_model3.updated_at.isoformat()))
        self.assertEqual(dict_test.get("created_at"),
                         str(base_model3.created_at.isoformat()))

    def test_save(self):
        """unittest"""
        base_model4 = BaseModel()
        time = base_model4.updated_at
        base_model4.save()
        self.assertGreater(base_model4.updated_at, time)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        base_model5 = BaseModel()
        hbnb_dict = base_model5.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "BaseModel")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         base_model5.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         base_model5.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
