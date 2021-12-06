#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The numver of elements to print from my_list.

       Returns:
              The number of elements printed.
    """
    count = 0
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            count += 1
    except Exception:
        print("", end="")

    print("")
    return count
