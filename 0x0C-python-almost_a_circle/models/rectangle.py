#!/usr/bin/python3
"""Defines a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The id of the new Rectangle.

        Raise:
            TypeError: If width or height is not an int.
            TypeError: If x or y coordinate is not an int.
            ValueError: If width or height is <= 0.
            ValueError: If x or y coordinate is < 0.

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the representation of the Rectangle with the character `#`"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        # Handling the y coordinate:
        [print("") for i in range(self.y)]

        for row in range(self.height):
            # Handling the x coordinate:
            print(" " * self.x, end="")
            for char in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Sets all rectangle attributes.

        Args:
            *args (ints): New attribute values
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
        """
        if len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            index = 0

            for attr in attrs:
                if index == len(args):
                    break
                setattr(self, attr, args[index])
                index += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
