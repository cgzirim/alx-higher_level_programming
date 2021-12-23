#!/usr/bin/python3
"""Defines a function that reads a file."""


def read_file(filename=""):
    """Prints the contents of a UTF-8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
