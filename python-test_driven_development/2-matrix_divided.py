#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Checks if the rows of the matrix have the same size
    and if they are int or float."""
    if len(matrix) > 1:
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
    else:
        for lista in matrix:
            for elemento in lista:
                if type(elemento) != int and type(elemento) != float:
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
    new_matrix = []
    for fila in matrix:
        new_fila = []
        for elemento in fila:
            new_elemento = round(elemento / div, 2)
            new_fila.append(new_elemento)
        new_matrix.append(new_fila)
    return(new_matrix)
