#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = a_dictionary.copy()
    for i in a_dictionary.keys():
        temp[i] = a_dictionary[i] * 2
    return temp
