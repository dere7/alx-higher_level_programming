#!/usr/bin/python3
"""
contains a base class that manages id attribute to remove
unnecessary redundancy.
"""


class Base:
    """base of all other :classes in this project. It
    manages id attribute in all classes and to avoid duplicating
    the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def integer_validator(name, value, isGreaterThanOrEqual=False):
        """Validates integer
        :raises: TypeError
        :raises: ValueError"""
        if type(value) is not int:
            raise TypeError(f'{name}  must be an integer')
        if value <= 0 and not isGreaterThanOrEqual:
            raise ValueError(f'{name} must be > 0')
        if isGreaterThanOrEqual and value < 0:
            raise ValueError(f'{name} must be >= 0')
