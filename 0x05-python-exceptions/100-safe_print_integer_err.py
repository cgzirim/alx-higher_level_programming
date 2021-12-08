#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer

    Args:
        value (int): Integer to print.

    Returns:
           If value is an integer - True.
           Otherwise - False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
