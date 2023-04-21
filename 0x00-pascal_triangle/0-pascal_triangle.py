#!/usr/bin/python3
"""a function to illustrate the inner workings of Pascal's Triangle"""


def pascal_triangle(n):
    """exits the code with an empty list if n is less than or equal to 0"""
    if n <= 0:
        return []

    triangle = [0]*n

    for i in range(n):
        """the line below creates a list of 0's with the length of i + 1"""
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1

        for j in range(1, i):
            """this creates a list of 0's with the length of i"""
            if j > 0 & j < i:
                """the line below adds two numbers from the previous row"""
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle[i] = row
    return triangle
