#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == None:
        return 0
    key = 0
    value = 0
    for i, x in my_list:
        key += i * x
        print("key = {}",key)
        value += x
        print("value = {}",value)
    return (key /value)
