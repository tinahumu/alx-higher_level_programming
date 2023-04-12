#!/usr/bin/python3

"""
Python Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        self.integer_validator("Width", width)
        self.integer_validator("Height", height)
        self.__width = width
        self.__height = height
