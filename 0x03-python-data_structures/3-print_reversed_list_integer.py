#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list, in reverse order."""

    for num in range(len(my_list)):
        print("{:d}".format(my_list.pop()))
