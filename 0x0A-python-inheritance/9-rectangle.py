#!/usr/bin/python3
"""defines rectangle class from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry with attributes height and width"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implements area"""
        return self.__height * self.__width

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
