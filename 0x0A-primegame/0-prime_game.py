#!/usr/bin/python3
"""
modu8le to save prime game
"""


def sieve(n):
    """
    checks all primes
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """
    finds out who wins
    """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    primes_up_to_max_n = sieve(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = [p for p in primes_up_to_max_n if p <= n]
        if not primes:
            ben_wins += 1
            continue
        moves = 0
        taken = [False] * (n + 1)
        while primes:
            current_prime = primes.pop(0)
            if not taken[current_prime]:
                moves += 1
                for multiple in range(current_prime, n + 1, current_prime):
                    taken[multiple] = True
                primes = [p for p in primes if not taken[p]]
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
