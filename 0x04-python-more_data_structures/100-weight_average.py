#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    n = 0
    if my_list == []:
        return 0
    for i in my_list:
        sum += i[0] * i[1]
        n += i[1]
    return sum / n
