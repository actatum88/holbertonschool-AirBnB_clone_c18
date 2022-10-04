#!/usr/bin/python3
"""Class FileStorage: serializes instances to a JSON file and deserializes JSON file to instances."""
import json
from models.base_model import BaseModel
from models.user import Amenity
from models.state import City
from models.city import Place
from models.place import Review
from models.amenity import State
from models.review import User

class_name = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
    }


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
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for o in json.load(f).values():
                    class_name = o['__class__']
                    del o['__class__']
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            pass
