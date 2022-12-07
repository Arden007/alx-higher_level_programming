#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = 0
    for i in set(my_list):
        uniq_num += i
    return uniq_num
