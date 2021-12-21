#!/usr/bin/python3
"""Define a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialze a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.

        Raises:
            TypeError - If either width or height is a negative
            integer or not an integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the new rectangle."""
        return(self.__width * self.__height)

    def __str__(self):
        """Print Rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
