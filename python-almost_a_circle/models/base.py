#!/usr/bin/python3
"""Write the first class Base."""


class Base:
    """Class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base."""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
