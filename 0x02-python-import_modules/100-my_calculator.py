#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def calculator(argv):
    i = len(argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    opperand = argv[2]
    b = int(argv[3])
    if opperand == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, opperand, b, add(a, b)))
    elif opperand == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, opperand, b, sub(a, b)))
    elif opperand == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, opperand, b, mul(a, b)))
    elif opperand == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, opperand, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if __name__ == "__main__":
    import sys
    calculator(sys.argv)
