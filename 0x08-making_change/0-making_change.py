#!/usr/bin/python3
"""
script for task 0
"""


def makeChange(coins, total):
    """
    function for task 0
    """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    few = 0
    for coin in coins:
        if total <= 0:
            break
        counter = total // coin
        few += counter
        total -= (counter * coin)
    if total != 0:
        return -1
    return few
