#!/usr/bin/python3
"""Defines an empty class."""


class Square:
    """Define a square class."""
    def __init__(self, size=0):
        """Defines a private instance attribute."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
