#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry():
    """Initialize BaseGeometry."""
    def area(self):
        """Raise a exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input value."""
        self.name = name
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        
