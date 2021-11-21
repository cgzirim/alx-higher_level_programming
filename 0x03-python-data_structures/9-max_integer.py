#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None

    max_num = my_list[0]

    for number in my_list:
        if max_num > number:
            continue
        else:
            max_num = number

    return max_num
