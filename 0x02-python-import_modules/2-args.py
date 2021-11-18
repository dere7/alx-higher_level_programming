#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    argLen = len(argv) - 1
    print('{:d} argument'.format(argLen), end='')
    if argLen == 1:
        print(':')
    elif argLen == 0:
        print('s.')
    else:
        print('s:')

    if argLen != 0:
        for i in range(1, len(argv)):
            print('{:d}: {:s}'.format(i, argv[i]))
