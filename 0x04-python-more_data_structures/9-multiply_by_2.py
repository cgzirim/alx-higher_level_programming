#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2"""
    new_directory = {k: v*2 for k, v in a_dictionary.items()}
    return new_directory
