#!/usr/bin/python3
"""Function that prints a square with the character #."""


def print_square(size):
    """Checks if size is valid and paints a square."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print()
    else:
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print()
