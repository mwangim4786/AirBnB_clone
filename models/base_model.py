#!/usr/bin/python3
"""
Defines a class BaseModel
"""


import uuid
from datetime import datetime


class BaseModel:
    """Representation of BaseModel"""
    def __init__(self):
        """Initializes the BaseModel
        
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # storage.new(self)


    def __str__(self):
        """prints human readable string representation of [<class name>] (<self.id>) <self.__dict__>"""
        
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the base model instance
        including __class__ representing the class name.
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict





