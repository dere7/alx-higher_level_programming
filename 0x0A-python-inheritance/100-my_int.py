#!/usr/bin/python3
"""defines MyInt that inherits int"""


class MyInt(int):
    """defines MyInt that inherits int"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
