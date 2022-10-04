#!/usr/bin/python3
""""Tests the file_storage module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Tests FileStorage class"""
    def setup(self):
        """Setup before each test"""
        self.fs = FileStorage()

    def tearDown(self):
        """clean up after each test"""
   pass
