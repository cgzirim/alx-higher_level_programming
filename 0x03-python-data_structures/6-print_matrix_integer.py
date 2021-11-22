#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for item in row:
            print("{:d}".format(item), end="")
            if row.index(item) != (len(row) - 1):
                print(" ", end="")
        print("")
