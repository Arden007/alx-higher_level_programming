#!/usr/bin/python3
def no_c(my_string):
    no_c_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            no_c_str += i
    return (no_c_str)
