#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Check if file to save list into exists or not.
if os.path.exists("add_item.json"):
    existing = load_from_json_file("add_item.json")
    for argument in sys.argv[1:]:
        existing.append(argument)
    save_to_json_file(existing, "add_item.json")
else:
    args = [elem for elem in sys.argv[1:]]
    save_to_json_file(args, "add_item.json")
