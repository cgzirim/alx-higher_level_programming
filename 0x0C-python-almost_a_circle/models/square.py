#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of the rectangle."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)

    def update(self, *args, **kwargs):
        """Sets all square attributes.
        Args:
            *args (ints): New attribute values
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3th argument should be the x attribute
                - 4th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            index = 0

            for attr in attrs:
                if index == len(args):
                    break
                setattr(self, attr, args[index])
                index += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
                'id': self.id,
                'size': self.height,
                'x': self.x,
                'y': self.y,
                }
