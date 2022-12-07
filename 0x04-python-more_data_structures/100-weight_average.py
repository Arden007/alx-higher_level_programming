#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    key = 0
    value = 0
    for i, x in my_list:
        key += i * x
        value += x
    return (key/value)
