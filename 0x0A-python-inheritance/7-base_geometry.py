#!/usr/bin/python3
"""defines a base geometry class"""


class BaseGeometry:
    """defines base geometry class with area() and integer_validator methods"""
    def area(self):
        """:raises: Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer
        :raises: TypeError
        :raises: ValueError"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
