#!/usr/bin/python3
"""contains a function that finds a peak in list"""


def find_peak(ls):
    """finds a peak in list"""
    for i in range(1, len(ls) - 1):
        if ls[i - 1] < ls[i] > ls[i + 1]:
            return ls[i]
