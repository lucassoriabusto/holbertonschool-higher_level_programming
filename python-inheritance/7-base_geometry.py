#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """The case is defined as BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value, must be an int and greater than 0"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
