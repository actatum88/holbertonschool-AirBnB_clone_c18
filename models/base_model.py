#!/usr/bin/python3
""" Base model Module """

import datetime
import uuid import uuid4
timestamp = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Creates Base Model, define attributes for project. """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
           """ Overriding __str__ to print custom string """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates public instance to current date/time """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
          """ Returing a dictionary containing all keys/values of __dict__ """
        newDict = dict(self.__dict__)
        newDict.update({"__class__": type(self).__name__})
        newDict.update({"updated_at": self.updated_at.isoformat()})
        newDict.update({"created_at": self.created_at.isoformat()})
        return newDict
