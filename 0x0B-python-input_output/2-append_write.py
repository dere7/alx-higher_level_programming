#!/usr/bin/python3
"""
contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """
    Reads a text file and prints to stdout
    :param text: a text to be appended
    :param filename: file name to read from
    :return: None
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
