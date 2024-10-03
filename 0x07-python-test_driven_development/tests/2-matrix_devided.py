#!/usr/bin/python3
"""Defines a matrix_divided function."""

def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (list): a list of lists of integers or floats
        div (int or float): the divisor.
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        ValueError: if matrix is not rectangular or if div is not a number
        ZeroDivisionError: if div is zero
    Returns:
        a new matrix
    """
    if (not isinstance(matrix, list) or matrix ==[] or 
        not all(isinstance(row, list) for row in matrix) or 
        not all((isinstance(i, int) or isinstance(i, float)) 
                for i in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a list of lists of integers or floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
