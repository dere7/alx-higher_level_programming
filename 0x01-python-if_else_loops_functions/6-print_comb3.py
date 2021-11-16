#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i == 8:
                print('{:02d}'.format(i * 10 + j), end='\n')
                break
            print('{:02d}'.format(i * 10 + j), end=', ')
