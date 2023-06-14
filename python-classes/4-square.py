#!/usr/bin/python3
"""Defines an empty class."""


class Square:
    """Define a square class."""
    def __init__(self, size=0):
        """Defines a private instance attribute."""
        self.__size = size

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
