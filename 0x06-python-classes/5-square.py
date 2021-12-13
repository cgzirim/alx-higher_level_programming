#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square.."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the new square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the character #"""
        for column in range(self.__size):
            for row in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")