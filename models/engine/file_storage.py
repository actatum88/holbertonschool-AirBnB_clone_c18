#!/usr/bin/python3
"""Class FileStorage: serializes instances to a JSON file
    and deserializes JSON file to instances."""
import json
from os import path


class FileStorage:
    """Class FileStorage with Private Class Attributes and
        Public Instance Methods"""

    # string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps({key: value.to_dict() for key, value
                                in self.__objects.items()}))

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        # manage serialization and deserialization of all classes
        class_names = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        # if the file doesn’t exist, no exception should be raised
        if not path.exists(self.__file_path):
            pass
        # if the file doesn’t exist, no exception should be raised
        elif path.getsize(self.__file_path) == 0:
            pass
        # deserializes the JSON file to __objects
        else:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                classes = class_names.get(key.split('.')[0])
                self.__objects[key] = classes(**value)
