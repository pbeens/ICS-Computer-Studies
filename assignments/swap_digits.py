'''
Swap digits
Given a two-digit number, swap its digits. If the returned value is less than 10, do not include the leading zero.
'''

import doctest

def swap_digits(n):
    """
    (int -> list of ints)
    :param n: int
    :return: int
    >>> swap_digits(23)
    32
    >>> swap_digits(60)
    6

    Enter your code below
    """

    return n

if __name__ == "__main__":
    doctest.testmod()

print(swap_digits(45))