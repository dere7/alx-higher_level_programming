#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = list(a_dictionary.keys())[0]
    for k, v in a_dictionary.items():
        if (a_dictionary[best_key] < v):
            best_key = k
    return best_key
