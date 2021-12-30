#!/usr/bin/python3
"""Defines a function that represents a pascal's triangle."""


def pascal_triangle(n):
    """Returns a  list of lists of integers representing the Pascal triangle.

    Args:
        n (int): Size of the Pascal triangle.
    """
    if n <= 0:
        return []

    p_t = [[1]]
    for i in range(1, n):
        row = []
        last_arr = p_t[-1]
        j = 0
        while j != len(last_arr):
            if j == 0:
                row.append(1)
            if j == (len(last_arr) - 1):
                row.append(1)
            else:
                row.append(last_arr[j] + (last_arr[j + 1]))
            j += 1
        p_t.append(row)
    return p_t
