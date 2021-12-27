#!/usr/bin/python3
"""contains a function that checks if an object is instance of a class"""


def inherits_from(obj, a_class):
    """
    checks if an obj is instance of class that is inherited from a_class
    :param obj: object
    :param a_class: a class
    :return: bool
    """
    return isinstance(obj, a_class) and obj.__class__ != a_class
