#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """def doc"""
    if list_of_integers:
        a = 0
        b = len(list_of_integers) - 1
        while a < b:
            m = (a + b) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                b = m
            else:
                a = m + 1
        return list_of_integers[a]
