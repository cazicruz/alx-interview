#!/usr/bin/python3
"""
Given an n x n 2D matrix, we are writing a code to
rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix clockwise 90 degrees"""
    container = []
    result =[]
    m = matrix
    length = len(matrix)
    for i in range(length):
        for value in m:
            new_value = value.pop(0)
            container.insert(0, new_value)
            #print (container)
        #matrix[i] = container
        result.append(container)
        container = []
    for i in range(length):
        matrix[i] = result[i]