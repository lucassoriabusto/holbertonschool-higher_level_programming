#!/usr/bin/python3
"""Write the first class Base."""


import json


class Base:
    """Class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
