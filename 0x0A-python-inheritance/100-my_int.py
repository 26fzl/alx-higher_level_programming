#!/usr/bin/python3
"""module the define a class MyInt"""


class MyInt(int):
    """classe."""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
