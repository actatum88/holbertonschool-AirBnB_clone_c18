#!/usr/bin/python3
""" Base model Module """

import datetime
import uuid
timestamp = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Creates Base Model, define attributes for project. """
    def __init__(self, *args, **kwargs):
        """ Initializes base instance. """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    timestamp)
                if key == 'updated_at':
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    timestamp)
                if key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        self.new = models.storage

    def __str__(self):
        """ Converts to message """
        message = "[{}] ({}) {}".format(self.__class__, self.id, self.__dict__)
        return message

    def save(self):
        """ Updates public instance to current date/time """
        self.updated_at = datetime.datetime.now()
        self.save = models.storage

    def to_dict(self):
        """ Returing a dictionary containing all keys/values of __dict__ """
        dict_cpy = self.__dict__.copy()
        dict_cpy['__class__'] = type(self).__class__.__name__
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        return dict_cpy