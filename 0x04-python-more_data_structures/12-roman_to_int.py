#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string == None:
        return 0
    convert = 0
    roman_dig = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in roman_string:
        rom_num = roman_dig[i]
        convert += rom_num if convert < rom_num * 5 else -rom_num
    return convert
