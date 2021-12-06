#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print in my_list.

    Returns:
           Number of integers printed.
    """

    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except Exception:
        print("", end="")

    print("")
    return count
