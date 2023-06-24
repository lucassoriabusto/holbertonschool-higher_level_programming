#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """Encoding (Serialization): Converts Python objects to a JSON string."""
    json_obj = json.dumps(my_obj)
    return json_obj
