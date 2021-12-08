#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists.

    Args:
        my_list_1 (list): Each element in this list serve as a dividend.
        my_lsit_2 (list): Each element in this list serve as a divisor.
        list_length (int): Number of elements to be divided.

    Returns:
           A new list (length = list_length) with all divisions.
    """
    quotients = []
    try:
        for i in range(list_length):
            try:
                res = my_list_1[i] / my_list_2[i]
                quotients.append(res)
            except TypeError:
                print("wrong type")
                quotients.append(0)
            except ZeroDivisionError:
                print("division by 0")
                quotients.append(0)
            except IndexError:
                print("out of range")
    finally:
        return quotients
