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
        self.size = size

    @property
    def size(self):
        '''
        get private variable size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        get private variable size
        Args:
            value (int): positive  integer to be stored to size
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        ''' returns area of the square '''
        return self.size ** 2

    def my_print(self):
        '''
        prints square offseted by position and using # character
        '''
        print() if self.size == 0 else None
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()
