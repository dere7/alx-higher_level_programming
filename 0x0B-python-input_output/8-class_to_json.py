#!/usr/bin/python3
"""
contains a function that returns the dictionary desc
"""


def class_to_json(obj):
    """
    returns a dic desc of simple data
    :param obj: object to be serialized
    :return: dict repr of object
    """
    return vars(obj)
