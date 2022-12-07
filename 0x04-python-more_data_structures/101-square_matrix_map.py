#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda key: list(map(lambda value: value * value, key)), matrix)))