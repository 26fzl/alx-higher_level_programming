#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """Return an  object representation of a JSON string."""
    return json.loads(my_str)
