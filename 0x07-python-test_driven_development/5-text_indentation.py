#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    wasBreak = False
    for i in text:
        if i in '.?:':
            wasBreak = True
            print(i)
            print()
        elif wasBreak and i == ' ':
            continue
        else:
            wasBreak = False
            print(i, end='')
