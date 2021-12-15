#!/usr/bin/python3


def add_integer(a, b=98):
    """Returns sum of two integers.

    Args:
        a (int): First number.
        b (int): Second number.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
       TypeError: If either a or b is non-integer or non-float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
