#!/usr/bin/python3
"""__init__ file for FileStorage"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
