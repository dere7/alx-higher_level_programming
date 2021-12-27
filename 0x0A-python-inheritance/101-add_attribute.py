#!/usr/bin/python3
"""contains a function that adds a new attribute to an object"""


def add_attribute(obj, key, value):
    """Sets the named attribute on the given object to the specified value.
    it is equivalent to ``x.y = v``
    """
    immutables = [int, float, bool, str, tuple, range]
    if type(obj) in immutables:
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
