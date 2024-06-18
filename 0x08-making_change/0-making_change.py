#!/usr/bin/python3
""" A module for making change"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make amount 0

    # Fill the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity,
    # it means it's not possible to make that amount
    return dp[total] if dp[total] != float('inf') else -1
