#!/usr/bin/python3
""" Base model Module """

import datetime
import uuid
timestamp = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Creates Base Model, define attributes for project """
    def __init__(self, uuid4):
        """ Initializes base instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        """ Overriding __str__ to print custom string """
        return ([<class name>] (<self.id>) <self.__dict__>)
