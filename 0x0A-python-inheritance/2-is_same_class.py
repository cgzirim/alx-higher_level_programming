#!/usr/bin/python3
"""Defines a function that compares an instance and a class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of  a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The type to match the type of obj to.

    Returns:
        If object is exactly an instance of class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
