#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Convertir el objeto a una cadena JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json_obj = json.dumps(my_obj)
        """Escribir la cadena JSON en el archivo"""
        f.write(json_obj)
