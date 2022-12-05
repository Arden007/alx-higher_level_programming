#!/usr/bin/python3
def no_c(my_string):
    no_c_str = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            no_c_str += i
    return (no_c_str)
