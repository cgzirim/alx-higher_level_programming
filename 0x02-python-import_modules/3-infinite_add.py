#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    """Print sum if all program's arguments"""

    numbers = [int(s) for s in sys.argv[1:]]
    print(sum(numbers))
