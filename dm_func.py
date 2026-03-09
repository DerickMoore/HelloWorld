"""Module for utility functions."""


def dm_hello(s):
    """Print the given string to console.

    Args:
        s: String to print
    """
    print(s)

def is_prime(n):
    """Check if a number is prime.

    Args:
        n: Integer to check

    Returns:
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True