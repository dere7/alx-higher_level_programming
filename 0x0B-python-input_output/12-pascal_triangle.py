#!/usr/bin/python3
"""
returns pascal triangle
"""


def pascal_triangle(n):
    """
    returns list of pascal triangle
    :param n: number of row
    :return: 2D list
    """
    pascal = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(row)
    return pascal
