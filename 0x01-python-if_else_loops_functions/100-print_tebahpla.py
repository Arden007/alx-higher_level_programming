#!/usr/bin/python3
i = 'z'
while i >= 'a':
    diff = 0
    if i % 2 != 0:
        i = i - 32
        diff = 1
    print("{:s}".format(chr(i)), end="")
    if diff == 1:
        i = i + 32
    i = i - 1
