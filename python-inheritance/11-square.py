#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py)."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Scuare that inherits the methods
    and properties of class Rectangl"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
    """Calculates the area of the scuare"""
    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
