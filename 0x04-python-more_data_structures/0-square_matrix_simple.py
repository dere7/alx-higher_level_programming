#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda i: list(map(lambda x: x * x, i)), matrix))
