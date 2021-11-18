#!/usr/bin/python3.8

if __name__ == "__main__":
    import hidden_4
    """Prints all names defined by hidden_4.pyc"""

    names = dir(hidden_4)

    for name in names:
        if name[:2] != '__':
            print(name)
