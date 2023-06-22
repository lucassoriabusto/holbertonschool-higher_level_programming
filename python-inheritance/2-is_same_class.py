#!/usr/bin/python3
"""Check if the object is exactly an instance of the specified clas."""


def is_same_class(obj, a_class):
    """If it is an instance return True, otherwise False."""
    if type(obj) == a_class:
        return True
    else:
        return False
