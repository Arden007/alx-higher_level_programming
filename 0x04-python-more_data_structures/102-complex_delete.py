#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    remove_keys = []
    for i in a_dictionary:
        if a_dictionary[i] is value:
            remove_keys.append(i)
    for i in remove_keys:
        del a_dictionary[i]
    return a_dictionary
