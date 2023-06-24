#!/usr/bin/python3
"""Write a class Student."""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor de la clase Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Devuelve una representación en forma de diccionario
        de la instancia de la clase Student."""
        return self.__dict__
