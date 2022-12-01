#!/usr/bin/python3
def num_arg(argv):
    count = len(argv) - 1
    if count == 0:
        print("{:d} argument.".format(count))
        return
    else:
        if count == 1:
            print("{:d} argument:".format(count))
        else:
            print("{:d} arguments:".format(count))
        i = 1
    for i in range(count):
        print("{:d}: {:s}".format(i + 1, argv[i + 1]))

if __name__ == "__main__":
    import sys
    num_arg(sys.argv)
