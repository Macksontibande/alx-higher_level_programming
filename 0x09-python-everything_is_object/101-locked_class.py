#!/usr/bin/python3
"""Program for a class LockedClass with no class or object attribute"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes
    """

    __slots__ = ["first_name"]
