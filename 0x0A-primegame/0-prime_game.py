#!/usr/bin/python3
"""Module defining isWinner function."""


def sieve_of_eratosthenes(limit):
    """Returns a list of prime numbers up to the limit
    using the Sieve of Eratosthenes algorithm."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    """Determine the winner of the prime game after x rounds."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes:
            prime_count[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
