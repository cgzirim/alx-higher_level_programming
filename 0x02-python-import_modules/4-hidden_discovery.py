#!/usr/bin/python3.8

if __name__ == "__main__":
    import hidden_4
    """Prints all names defined by hidden_4.pyc"""

    names = [x for x in dir(hidden_4) if not x.startswith('__')]

    for name in names:
        print(name)
