#!/usr/bin/python3
"""
script for task 0
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    """
    if not isinstance(n, int):
        return 0
    op_c = 0
    clip = 0
    d = 1
    while d < n:
        if clip == 0:
            clip = d
            d += clip
            op_c += 2
        elif n - d > 0 and (n - d) % d == 0:
            clip = d
            d += clip
            op_c += 2
        elif clip > 0:
            d += clip
            op_c += 1
    return op_c
