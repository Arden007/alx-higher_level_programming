#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    for i in matrix:
        temp.append(list(map(lambda i: i**2, i)))
    return temp
