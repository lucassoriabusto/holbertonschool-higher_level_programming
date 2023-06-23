#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Squear that inherits from Rectangle"""

    def __init__(self, size):
        """Initialization the size."""
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """Returns the area."""
        return self.__size ** 2

    def __str__(self):
        """Prints the dimensions of the square."""
        return(f"[Square] {self.__size}/{self.__size}")
