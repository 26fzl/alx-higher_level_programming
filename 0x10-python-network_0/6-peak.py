#!/usr/bin/python3
""" Finds a peak """

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    mid_e = size
    mids = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mids < size - 1 and
                list_of_integers[mids] < list_of_integers[mids + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mids = mids + mid_e // 2
        elif mid_e > 0 and list_of_integers[mids] < list_of_integers[mids - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mids = mids - mid_e // 2
        else:
            return list_of_integers[mids]
