#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    
    def __init__(self, width, height):
        """Initialization with width and height"""
        self.__width = width
        self.__height = height
        """Calls the inherited method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
