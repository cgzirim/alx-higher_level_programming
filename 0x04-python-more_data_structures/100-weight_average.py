#!/usr/bin/python3


def weight_average(my_list=[]):
    """Return the weighted average of all integers tuple."""
    x = 0
    y = 0
    if len(my_list) == 0:
        return 0

    for tple in my_list:
        x += tple[0] * tple[1]
        y += tple[1]
    return (x / y)
