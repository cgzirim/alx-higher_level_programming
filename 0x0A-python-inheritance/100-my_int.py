#!/usr/bin/python3
"""Define a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts == and != operators."""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behaviour."""
        return self.real == value
