#!/usr/bin/python3
""" module of the function """


def add_attribute(obj, atr, value):
    """function that adds attributes to objects. """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
