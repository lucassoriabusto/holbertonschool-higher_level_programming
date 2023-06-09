#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        new_matriz = []
        for row in matrix:
            new_row = []
            for element in row:
                new_element = element ** 2
                new_row.append(new_element)
            new_matriz.append(new_row)
        return new_matriz
