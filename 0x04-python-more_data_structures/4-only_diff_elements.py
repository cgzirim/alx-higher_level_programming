#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Teturn a set of all elements present in only one set."""
    return set(set_1 ^ set_2)
