#!/usr/bin/python3
"""Define function that checks if an object
is directly or indirectly inherited from a class."""


def inherits_from(obj, a_class):
    """Checks if an object is directly or
    indirectly inherited from a class.

    Args:
        obj (any): The object of an instance.
        a_class: The class.

    Returns:
       True - if the obj is an instance of a class that
inherited (directly or indirectly) from the specified class.
       Otherwise - False.
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
