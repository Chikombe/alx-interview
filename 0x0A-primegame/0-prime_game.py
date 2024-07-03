#!/usr/bin/python3

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if primes[p]]
    return prime_numbers


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Simulate the game
        if n < 2:
            ben_wins += 1
            continue

        game_state = [True] * (n + 1)
        game_state[0] = game_state[1] = False

        current_player = "Maria"
        while True:
            move_made = False
            for prime in primes:
                if prime > n:
                    break
                if game_state[prime]:
                    move_made = True
                    for multiple in range(prime, n + 1, prime):
                        game_state[multiple] = False
                    break

            if not move_made:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            current_player = "Ben" if current_player == "Maria" else "Maria"

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
