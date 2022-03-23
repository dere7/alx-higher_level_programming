#!/usr/bin/python3
"""contains a function that finds a peak in list"""


def find_peak(lst):
    """finds a peak in list"""
    start, end = 0, len(lst) - 1
    while start < end:
        mid = start + (end - start) // 2

        # Check if it's a peak
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]
        if len(lst) == 3 and lst[mid] == lst[mid-1] == lst[mid+1]:
            return lst[mid]
        if lst[mid - 1] > lst[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return None
