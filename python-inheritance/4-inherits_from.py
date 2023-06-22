#!/usr/bin/python3
"""Function that returns True if the object is an
instance of a class that inherited."""


def inherits_from(obj, a_class):
    """Returns True if it is, False otherwise."""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
