#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastnum = number % -(10)
        print(-(lastnum), end='')
    else:
        lastnum = number % 10
        print(lastnum, end='')
    return lastnum
