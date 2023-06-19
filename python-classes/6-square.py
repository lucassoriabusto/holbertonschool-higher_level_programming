#!/usr/bin/python3
"""Defines an empty class."""


class Square:
    """Define a square class."""
    def __init__(self, size=0, position=(0, 0)):
        """Defines a private instance attribute."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute."""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0] != int) or (value[1] != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for p in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
