#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""

    if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
        len_a = len(tuple_a)
        len_b = len(tuple_b)
        # If both tuples are empty assign (0,0) to each.
        if len_a == 0:
            tuple_a = 0, 0
        if len_b == 0:
            tuple_b = 0, 0

        # If either tuples have 1 arg, assign 0 as the second arg.
        if len_a == 1:
            a = tuple_a[0]
            tuple_a = a, 0
        if len_b == 1:
            b = tuple_b[0]
            tuple_b = b, 0

        # Return the sum of tuples in the format (a,b)
        a0, a1 = tuple_a
        b0, b1 = tuple_b

        x = a0 + b0
        y = a1 + b1
        t = x, y

        return (t)
