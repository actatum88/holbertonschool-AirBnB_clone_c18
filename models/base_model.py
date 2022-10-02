#!/usr/bin/python3
"""Class BaseModel: defines all common attributes/methods for other classes."""
from models.engine.file_storage import FileStorage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class BaseModel with Public Instance Attributes and Methods
        -if kwargs is not empty:
            -each key of this dictionary is an attribute name
            -each value of this dictionary is the value of this attribute name
        -otherwise
            -create id, created_at, and updated_at
    """
    def __init__(self, *args, **kwargs):
        """Instantiation of BaseModel"""
        timestamp = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, timestamp)
                if k == '__class__':
                    continue
                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Should Print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the Public Instance Attribute: updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a Dictionary Containing All Keys/Values of __dict__ of the Instance:
          -by using self.__dict__, only instance attributes set will be returned
          -a key __class__ must be added to this dictionary with the class name of the object
          -created_at and updated_at must be converted to string object in ISO format:
              -format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
              -you can use isoformat() of datetime object
          -this method will be the first piece of the serialization/deserialization process:
              create a dictionary representation with “simple object type” of our BaseModel
        """
        hbnb_dict = dict(self.__dict__)
        hbnb_dict['create_at'] = self.created_at.isoformat()
        hbnb_dict['updated_at'] = self.updated_at.isoformat()
        hbnb_dict['__class__'] = self.__class__.__name__
        return hbnb_dict
