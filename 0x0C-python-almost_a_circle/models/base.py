#!/usr/bin/python3
"""Defines a class Base."""
import json
from os.path import exists


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of `Base` inherited objects.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the Python representation of a JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            If json_string is None or an empy list - an empty list.
            Otherwise - the JSON deserialized string.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance initialized from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(height=3, width=2, x=0, y=0, id=None)
            if cls.__name__ == "Square":
                instance = cls(size=4, x=0, y=0, id=None)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances initialized from a file of JSON strings
        """
        filename = cls.__name__ + ".json"
        if exists(filename) is False:
            return []

        with open(filename, "r") as f:
            list_dicts = Base.from_json_string(f.read())

        list_objs = [cls.create(**dictionary) for dictionary in list_dicts]
        return list_objs
