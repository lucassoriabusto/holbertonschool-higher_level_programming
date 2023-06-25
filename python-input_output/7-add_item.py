#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
"""Get the command-line arguments."""

filename = "add_item.json"

if exists(filename):
    """Check if the file already exists."""
    my_list = load_from_json_file(filename)
    """Load the existing list from the file."""
else:
    my_list = []
    """If the file doesn't exist, create an empty list."""

my_list.extend(arguments)
"""Add the arguments to the list."""

save_to_json_file(my_list, filename)
"""Save the list as JSON in the file."""
