#!/usr/bin/python3


def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character."""
    length = len(sentence)

    if length == 0:
        first = None
    else:
        first = sentence[0]

    return (length, first)
