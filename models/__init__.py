#!/usr/bin/python3
"""__init__ file for FileStorage"""
from .engine.file_storage import FileStorage
from models import base_model
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
