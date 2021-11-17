#!/usr/bin/python3

"""Prints a string in uppercase followed by a new line."""


def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            ucase = chr(ord(letter) - 32)
        else:
            ucase = letter
        print("{}".format(ucase), end="")
    print("")
