#!/usr/bin/python3
"""Pascal's Triangle"""
def generate_pascals_triangle(n):
    """
    function def pascal_triangle(n): that returns a list of lists 
    of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
