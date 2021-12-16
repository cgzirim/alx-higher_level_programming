#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Raise:
         TypeError: If any element in matric isnt an integer or float.
                    If all rows in matrix are not of the same size.
                    If div isnt an integer or float.
         ZeroDivisionError: If div is equal to zero.
    """

    if not isinstance(matrix, list) or len(matrix) <= 1 or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    """if matrix <= 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")"""

    new_matrix = []
    row_size = len(matrix[0])

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

        for num in row:
            if not isinstance(num, int) or isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round((num / div), 2))
        if len(new_row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(new_row)
    return new_matrix
