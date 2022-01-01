#!/usr/bin/python3
"""Defines a class Base."""
import json


class Base:
    """Serves as a base class to other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize this class."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
