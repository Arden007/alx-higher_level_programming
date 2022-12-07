#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = list(map(lambda key: list(map(lambda value: value * value, key)), matrix))
    return new_list