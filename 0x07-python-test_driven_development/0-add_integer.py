#!/usr/bin/python3
"""

This is a function that will add 2 integer and act as a module

"""

def add_integer(a, b=98):
    """
    Add 2 integer args a & b

    Args:
        a(type int/float): first integer value
        b(type int/float): second integer value
    Raises:
    TypeError: when parameters/args passed are not type int/float

    Returns:
        type(int): the sum of the two integer args

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return(int(a)+int(b))
