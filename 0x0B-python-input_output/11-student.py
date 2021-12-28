#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, retrieve only those attributes
        includeded in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with elements of a dictionary.

        The dictionary key will be the public attribute name.
        The dictionary value will be the value of the public attribute.

        Args:
            json (dict): The dictionary.
        """
        for k, v in json.items():
            setattr(self, k, v)
