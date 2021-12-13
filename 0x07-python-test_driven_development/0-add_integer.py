#!/usr/bin/python3
'''This modules contain a function that adds 2 integers
a and b must be integers or float
if either of them are float they are casted to integer
if neither of them area float or int TypeError is thrown
'''


def add_integer(a, b=98):
    '''adds 2 integers
    Args:
        a (int): first integer
        b (int): second integer defualt 98
    Return: sum of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
