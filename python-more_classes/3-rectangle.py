#!/usr/bin/python3
"""Defines an empty class rectangle"""


class Rectangle:
    """The case is defined as rectangle"""
    def __init__(self, width=0, height=0):
        """Defines a private instance attribute."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for x in range(self.__height):
                for y in range(self.__width):
                    rectangle += "#"
                rectangle += "\n"
            return rectangle[:-1]
