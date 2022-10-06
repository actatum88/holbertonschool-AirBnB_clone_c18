#!/usr/bin/python3
"""Class BaseModel: defines all common attributes/
    methods for other classes."""
import models
from uuid import uuid4
from datetime import datetime

# created_at and updated_at must be converted to
# string object in ISO format
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Class BaseModel with Public Instance Attributes and Methods
        -if kwargs is not empty:
            -each key of this dictionary is an attribute name
            -each value of this dictionary is the value
                of this attribute name
        -otherwise
            -create id, created_at, and updated_at
    """

    # *args won’t be used
    def __init__(self, *args, **kwargs):
        """Instantiation of BaseModel"""
        # if kwargs is not empty
        if kwargs:
            # each key of this dictionary is an attribute name
            # each value of this dictionary is the value of this attribute name
            for key, value in kwargs.items():
                # __class__ from kwargs is the only one that
                # should not be added as an attribute
                if key != '__class__':
                    setattr(self, key, value)
            # must be converted to string object in ISO format, checking
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], time_format)
            # must be converted to string object in ISO format, checking
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], time_format)
        # otherwise, create id and created_at and updated_at
        else:
            # string - assign with an uuid when an instance is created
            self.id = str(uuid4())
            # datetime - assign with the current datetime
            # when an instance is created
            self.created_at = datetime.now()
            # datetime - and it will be updated every
            # time you change your object
            self.updated_at = datetime.now()
            # new instance, call to the method new(self) on storage
            models.storage.new(self)

    def __str__(self):
        """Should Print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the Public Instance Attribute:
            updated_at with the current datetime"""
        self.updated_at = datetime.now()
        # new instance, call to the method new(self) on storage
        models.storage.new(self)
        # call save(self) method of storage
        models.storage.save()

    def to_dict(self):
        """
        Returns a Dictionary Containing All Keys/
            Values of __dict__ of the Instance:
          -by using self.__dict__, only instance attributes
            set will be returned
          -a key __class__ must be added to this dictionary
            with the class name of the object
          -created_at and updated_at must be converted to string
            object in ISO format:
              -format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
              -you can use isoformat() of datetime object
          -this method will be the first piece of the serialization/
            deserialization process:
              create a dictionary representation with “simple object type”
                of our BaseModel
        """
        # first piece of the serialization/deserialization process
        # by using self.__dict__, only instance attributes set will be returned
        hbnb_dict = self.__dict__.copy()
        if 'created_at' in hbnb_dict:
            hbnb_dict['created_at'] = self.created_at.isoformat()
        if 'updated_at' in hbnb_dict:
            hbnb_dict['updated_at'] = self.updated_at.isoformat()
        # a key __class__ must be added to this dictionary with
        # the class name of the object
        hbnb_dict['__class__'] = self.__class__.__name__
        # returns a dictionary containing all keys/values
        # of __dict__ of the instance
        return hbnb_dict
