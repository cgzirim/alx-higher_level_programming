#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)."""
    total = 0
    unique = {number for number in my_list}
    for num in unique:
        total += num
    return total
