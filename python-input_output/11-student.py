#!/usr/bin/python3
"""Returns a dictionary representation of the Student instance."""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor de la clase Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """If attrs is a list of strings,
        only the specified attribute names are retrieved.
        Otherwise, all attributes are retrieved."""
        if isinstance(attrs, list):
            selected_attributes = {}
            for attribute in attrs:
                if hasattr(self, attribute):
                    selected_attributes[attribute] = getattr(self, attribute)
            return selected_attributes
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student
        instance using a JSON dictionary."""""
        return self.__dict__.update(json)
