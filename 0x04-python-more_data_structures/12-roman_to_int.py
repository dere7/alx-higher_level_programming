#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    on = 0
    for i, r in enumerate(roman_string):
        if on != 0:
            on = 0
            continue
        curr = roman_dic[r]
        if r in 'CXI' and i != len(roman_string) - 1:
            nex = roman_dic[roman_string[i+1]]
            if curr >= nex:
                num += curr
            else:
                num += nex - curr
                on = 1
        else:
            num += curr
    return num
