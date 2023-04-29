#!/usr/bin/python3
"""
    Program for a function that returns the list of available 
    attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: initial object
        
    Returns: a list of available attributes and
        methods of an object
    """
    return dir(obj)
