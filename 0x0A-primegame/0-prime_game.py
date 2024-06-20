#!/usr/bin/python3
"""
modu8le to save prime game
"""


def isWinner(x, nums):
    """
    finds out who wins
    """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    is_prime = [True for _ in range(max(max_n + 1, 2))]
    for a in range(2, int(pow(max_n, 0.5)) + 1):
        if not is_prime[a]:
            continue
        for b in range(a * a, max_n + 1, a):
            is_prime[b] = False
    is_prime[0] = is_prime[1] = False
    cume_p = 0
    for a in range(len(is_prime)):
        if is_prime[a]:
            cume_p += 1
        is_prime[a] = cume_p
    win = ''
    sc = 0
    for n in nums:
        sc += is_prime[n] % 2 == 1
    if sc * 2 == len(nums):
        win = None
    if sc * 2 > len(nums):
        win = "Maria"
    else:
        win = "Ben"
    return win
