#!/usr/bin/python3
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes into a UTF-8 text file."""

    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
