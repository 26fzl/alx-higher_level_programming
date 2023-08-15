#!/usr/bin/python3
"""Pascal's Triangle"""
def generate_pascals_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.
    :param n: Number of rows in the Pascal's Triangle.
    :return: A list containing Pascal's Triangle up to the specified number of rows.
    """
    if n <= 0:
        return []

    triangle = []
    for x in range(n):
        row = []
        for y in range(x):
            if len(row) == 0:
                row.append(1)
                continue
            value = triangle[x-1][y-1] + triangle[x-1][y]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
