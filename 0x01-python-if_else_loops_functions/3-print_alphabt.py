#!/usr/bin/python3

"""Print alphabet in lower case except from e and q."""
for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    print("{}".format(chr(letter)), end="")
