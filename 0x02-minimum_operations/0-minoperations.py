#!/usr/bin/python3
"""
script for task 0
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    """
    if n <= 1:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        if n % i == 0:
            dp[i] = min(dp[i], dp[n // i] + i)
        for j in range(1, i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j] + 1)
    return dp[n]
