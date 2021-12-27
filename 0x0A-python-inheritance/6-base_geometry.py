#!/usr/bin/python3
"""defines a base geometry class"""


class BaseGeometry:
    """defines base geometry class with area() and integer_validator methods"""
    def area(self):
        """:raises: Exception"""
        raise Exception("area() is not implemented")
