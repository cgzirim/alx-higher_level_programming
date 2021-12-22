#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Define the size of the class."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    def __str__(self):
        """Print the description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
