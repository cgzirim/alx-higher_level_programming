#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list without modifying the original list"""

    if isinstance(my_list, list):
        if idx >= 0 and idx < len(my_list):
            """If my_list is a list and idx isn't out of range then do:"""
            copy = my_list[:]
            copy[idx] = element
            return copy

    return my_list
