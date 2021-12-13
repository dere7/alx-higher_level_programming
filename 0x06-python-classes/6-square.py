#!/usr/bin/python3
'''
square classes that defines a square.
'''


class Square:
    '''
        Square defines a sqaures
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Args:
            size (int): positive size of the square
            position(tuple): pair of two positive integers that is used
            as ofset before print
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        ''' gets position of the square.'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' sets position of square which offsets the the square that will be drawn
            Args:
                value (tuple): pair of x and y which are positive integers
        '''
        if len(value) != 2 or type(value[0]) is not int or \
                type(value[1]) is not int or value[0] < 0 \
                or value[1] < 0 or type(value) is not tuple:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' returns area of the square '''
        return self.size ** 2

    def my_print(self):
        '''
        prints square offseted by position and using # character
        '''
        print() if self.size == 0 else None
        print('\n' * self.position[1], end='')
        for i in range(self.size):
            print(' ' * self.position[0], end='')
            for j in range(self.size):
                print('#', end='')
            print()
