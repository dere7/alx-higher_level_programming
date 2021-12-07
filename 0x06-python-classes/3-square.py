#!/usr/bin/python3
'''
square classes that defines a square.
'''


class Square:
    '''
        Square defines a sqaures
    '''
    def __init__(self, size=0):
        '''
        Args:
            size (int): positive size of the square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        ''' returns area of the square '''
        return self.__size ** 2
