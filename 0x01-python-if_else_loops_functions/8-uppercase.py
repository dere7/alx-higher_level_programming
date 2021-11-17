#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            j = ord(i) - ord('a') + ord('A')
        else:
            j = ord(i)
        print("{:c}".format(j), end='')
    print('')
