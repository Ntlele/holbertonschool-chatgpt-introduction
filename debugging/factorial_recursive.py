#!/usr/bin/python3
import sys

def factorial(n):
    """

    Function Description:
    Calculates the factorial of a given integer.

    Parameters:
    n (int): The integer for which factorial needs to be calculated.

    Returns:
    int: The factorial of the input integer.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
