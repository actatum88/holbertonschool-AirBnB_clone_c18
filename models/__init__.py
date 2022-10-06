#!/usr/bin/python3
"""__init__ file for FileStorage"""
from .engine.file_storage import FileStorage


# instance of FileStorage
storage = FileStorage()
# call reload() to FileStorage
storage.reload()
