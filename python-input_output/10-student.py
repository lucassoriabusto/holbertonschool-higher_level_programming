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
            """Para verificar si attrs es una lista."""
            selected_attributes = {}
            for attribute in attrs:
                if hasattr(self, attribute):
                    """Para verificar si el objeto self tiene el
                    atributo especificado en la variable attribute."""
                    selected_attributes[attribute] = getattr(self, attribute)
                    """Para obtener el valor del atributo especificado en la
                    variable attribute del objeto self."""
            return selected_attributes
        else:
            return self.__dict__
