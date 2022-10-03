#!/usr/bin/python3
"""Class FileStorage: serializes instances to a JSON file and deserializes JSON file to instances."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage with Private Class Attributes and Public Instance Methods"""

    def __init__(self):
        """Instantiation of FileStorage"""
        # string - path to the JSON file (ex: file.json)
        self.__file_path = "file.json"
        # dictionary - empty but will store all objects by <class name>.id
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_class = type(obj).__name__
        self.__objects["{}.{}".format(obj_class, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        hbnb_dict = self.__objects
        obj_dict = {obj: hbnb_dict[obj].to_dict() for obj in hbnb_dict.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    class_name = o['__class__']
                    del o['__class__']
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
