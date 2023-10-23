#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
import os

class FileStorage:
    """Class to serialize and deserialize base classes.

    Attributes:
        __file_path (str): The name of the file where objects are saved.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """set in __objects the obj with key <obj class name>.id"""
        obj_name = type(obj).__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        the_objects = FileStorage.__objects
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_data = {key: value.to_dict() for key, value in the_objects.items()}
            json.dump(dict_data, f)

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for key, value in obj_dict.items():
                    cls_name = value.get('__class__')
                    obj = eval(cls_name + '(**value)')
                    FileStorage.__objects[key] = obj
        