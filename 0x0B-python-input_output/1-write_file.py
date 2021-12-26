#!/usr/bin/python3
"""
contains a function that writes a text
"""


def write_file(filename="", text=""):
    """
    writes a text to a file
    :param filename: filename to write to
    :param text: text to be written
    :return: number of characters written
    """
    chars = 0
    with open(filename, "w", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
