#!/usr/bin/python3
"""Checks whether it is an instance or an instance of an inherited class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the given class is the subclass of given class"""
    return isinstance(obj, a_class)
