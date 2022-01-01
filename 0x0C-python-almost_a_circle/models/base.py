#!/usr/bin/python3
"""Defines a class Base."""


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
