#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argcount = len(sys.argv) - 1
    if argcount == 0:
        print("{:d} argument.".format(argcount))
    elif argcount == 1:
        print("{:d} argument.".format(argcount))
    else:
        print("{:d} argument.".format(argcount))
    for i in range(argcount):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
