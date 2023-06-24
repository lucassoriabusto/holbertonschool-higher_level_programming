#!/usr/bin/python3
"""Function that returns an object (Python data structure)
represented by a JSON string"""


import json


def from_json_string(my_str):
    """Decoding (Deserialization): Converts a JSON
    string into Python objects."""
    return json.loads(my_str)
