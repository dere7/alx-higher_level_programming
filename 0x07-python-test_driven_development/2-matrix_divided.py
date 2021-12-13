#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/\
         floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = []
    size = len(matrix[0])
    for i in matrix:
        if size != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        if type(i) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
        res = []
        for j in range(len(i)):
            if type(i[j]) is not int and type(i[j]) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
            res.append(round(i[j] / div, 2))
        result.append(res)
    return result
