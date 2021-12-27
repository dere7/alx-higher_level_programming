#!/usr/bin/python3
"""contains a function that checks if an object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    checks if an obj is instance of a_class or any parent class
    :param obj: object
    :param a_class: a class
    :return: bool
    """
    return isinstance(obj, a_class)
