#!/usr/bin/python3
"""Class FileStorage: serializes instances to a JSON file and deserializes JSON file to instances."""
import json
import os


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
        hbnb_dict = {}
        for k in self.__objects.items():
            hbnb_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(hbnb_dict, f)

    def class_model(self):
        """"""
        from models.base_model import BaseModel
        # from models.amenity import
        # from models.city import
        # from models.place import
        # from models.review import
        # from models.state import
        # from models.user import

        class_model = {
            "BaseModel": BaseModel
            # "Amenity":
            # "City":
            # "Place":
            # "Review":
            # "State":
            # "User":
        }
        return class_model

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        class_model = self.class_model()
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                class_name = v["__class__"]
                self.__objects[k] = class_model[class_name](**v)
