#!/usr/bin/python3
"""defines subclasses of list"""


class MyList(list):
    """inherits list class"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
