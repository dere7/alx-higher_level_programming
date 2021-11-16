#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            print("{:c}".format(ord(i) - ord('a') + ord('A')), end='')
        else:
            print(i, end='')
    print('')
