#!/usr/bin/python3
"""Defines a function that eads a file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename - File to be read.
    """
    with open(filename, 'r') as f:
        print(f.read())
    f.close()
