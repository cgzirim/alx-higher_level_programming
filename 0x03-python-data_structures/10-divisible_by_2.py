#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""
    booleans = []

    for number in my_list:
        if number % 2 == 0:
            booleans.append(True)
        else:
            booleans.append(False)

    return booleans
