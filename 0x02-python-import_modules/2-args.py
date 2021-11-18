#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    """Print number and list of program's arguments"""

    length = len(sys.argv)

    if length <= 1:
        print("0 arguments")
    elif length == 2:
        print("1 argument")
    else:
        print("{} argument:".format(length - 1))
        for arg in range(1, length):
            print("{}: {}".format(arg, sys.argv[arg]))
