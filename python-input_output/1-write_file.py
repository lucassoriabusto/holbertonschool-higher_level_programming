#!/usr/bin/python3
"""Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Open the file in write mode."""
    with open(filename, "w", encoding="utf-8") as f:
        """Write the content to the file"""
        f.write(text)
        return len(text)
