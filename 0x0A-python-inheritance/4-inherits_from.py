#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class."""
    return isinstance(obj, a_class) and not type(obj) is a_class
