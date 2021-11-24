#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    new_dict = a_dictionary
    rmv = []
    for k, v in new_dict.items():
        if v == value:
            rmv.append(k)
    for key in rmv:
        del new_dict[key]

    return new_dict
