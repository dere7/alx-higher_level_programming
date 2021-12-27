#!/usr/bin/python3
"""defines the function that checks if the object is exactly
instance of particular class"""


def is_same_class(obj, a_class):
    """checks if the object is exactly instance of particular class
    :param obj: any
    :param a_class: class
    :return: bool
    """
    return obj.__class__ == a_class
