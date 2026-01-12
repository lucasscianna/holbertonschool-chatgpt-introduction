#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Function:
        Computes the factorial of a non-negative integer n using recursion.
        The factorial of 0 is defined as 1. For any other positive integer n,
        factorial(n) = n * factorial(n-1).

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Compute factorial from command-line argument and print it
f = factorial(int(sys.argv[1]))
print(f)
