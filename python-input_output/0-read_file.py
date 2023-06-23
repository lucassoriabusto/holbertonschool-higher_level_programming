#!/usr/bin/python3
"""Function that reads a text file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout."""
    with open("my_file_0.txt", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
