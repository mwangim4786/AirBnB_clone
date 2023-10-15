#!/usr/bin/python3
"""
Defines a class BaseModel
"""


import uuid
from datetime import datetime


class BaseModel:
    """Representation of BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        


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