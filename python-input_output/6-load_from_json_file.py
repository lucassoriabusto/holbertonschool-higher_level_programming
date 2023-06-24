#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”."""


import json


def load_from_json_file(filename):
    """Load JSON data from a file and return the corresponding Python object"""
    with open(filename, encoding="utf-8") as f:
        json_obj = f.read()
        return json.loads(json_obj)
