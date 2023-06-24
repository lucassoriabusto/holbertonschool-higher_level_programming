#!/usr/bin/python3
"""Function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """("a") opens file in append mode."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
