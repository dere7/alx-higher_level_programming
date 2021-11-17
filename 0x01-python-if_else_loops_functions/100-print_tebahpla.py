#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        j = i - ord('a') + ord('A')
    else:
        j = i
    print("{:c}".format(j), end="")
