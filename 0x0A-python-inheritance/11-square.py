#!/usr/bin/python3
"""defines square class from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """subclass of Recatangle with attributes size"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
