#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("{} argument.".format(n))
    elif n == 1:
        print("{} argument.".format(n))
    else:
        print("{} argument.".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
