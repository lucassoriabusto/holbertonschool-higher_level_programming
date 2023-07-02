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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON representation of a list of objects in a f

        cls (class): La clase misma (Base) como parámetro implícito.
        list_objs (list): Lista de objetos heredados de la clase Base."""
        if list_objs is None:
            list_objs = []

        """Obtiene el nombre de la clase y le agrega la extensión .json."""
        class_name = cls.__name__
        filename = f"{class_name}.json"

        """Itera sobre la lista de objetos y
        obtiene el diccionario de cada objeto."""
        obj_dicts = []
        for obj in list_objs:
            obj_dicts.append(obj.to_dictionary())

        """Convierte la lista de diccionarios en una cadena JSON."""
        json_string = cls.to_json_string(obj_dicts)
        with open(filename, "w") as file:
            file.write(json_string)
