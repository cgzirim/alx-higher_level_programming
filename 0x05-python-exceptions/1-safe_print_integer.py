#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value: The input can be any type (integer, string, etc.)

    Returns:
           True if value is an integer.
           Otherwise, False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("", end="")
        return False
