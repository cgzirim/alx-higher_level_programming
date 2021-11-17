#!/usr/bin/python3


def fizzbuzz():
    """Prints the numbers from 1 to 100 separated by a space."""
    """For multiples of three print Fizz & for multiples of five - Buzz."""
    """For multiples of both three & five - FizzBuzz."""

    for number in range(1, 101):
        if (number % 15) == 0:
            print("FizzBuzz ", end="")
        elif (number % 5) == 0:
            print("Buzz ", end="")
        elif (number % 3) == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(number), end="")
