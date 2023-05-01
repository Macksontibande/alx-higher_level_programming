#!/usr/bin/python3
"""Module for a function that multiplies 2 matrices.
"""


def max_integer(list=[]):
    """function that multiplies 2 matrices.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
