#!/usr/bin/python3
"""  module that Defines a Rectangle subclass Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class that represent square """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
