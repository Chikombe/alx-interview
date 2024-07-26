#!/usr/bin/python3

"""
This module provides a function to compute the minimum number of operations
needed to achieve exactly n 'H' characters starting from 1 using only
"Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly
    n characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Factorize n to find the sum of its prime factors
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
