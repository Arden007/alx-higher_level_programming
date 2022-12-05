#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if 0 > idx > len(my_list):
            return my_list
        else:
            temp_list = my_list[:]
            temp_list[idx] = element
            return (temp_list)
