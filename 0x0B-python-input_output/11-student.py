#!/usr/bin/python3
"""Student to disk and reload"""

class Student:
    """Write a class Student """

     def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}

    def reload_from_json(self, json):
        self.__dict__.update(json)
