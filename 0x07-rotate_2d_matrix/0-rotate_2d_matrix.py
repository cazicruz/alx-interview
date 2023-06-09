#!/usr/bin/python3
"""
Given an n x n 2D matrix, we are writing a code to
rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    container = []
    result =[]
    length = len(matrix)
    for i in range(length -1):
        for value in matrix:
            new_value = value.pop(0)
            container.append(new_value)
        result.append(container)
    metrix = result
    yield metrix
