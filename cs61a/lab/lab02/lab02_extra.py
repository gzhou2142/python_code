"""Optional program for lab02 """

from lab02 import *

# Extra Question

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    i = 0
    def hailstone_helper(n):
        if n == 1:
            print(n)
        elif n % 2 == 0:
            print(n)
            hailstone_helper(n//2)
        else:
            print(n)
            hailstone_helper(3 * n + 1)
        nonlocal i
        i += 1
    
    hailstone_helper(n)
    return i

def count_cond(condition):
    """
    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2) # 1, 2
    2
    >>> count_factors(4) # 1, 2, 4
    3
    >>> count_factors(12) # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2) # 2
    1
    >>> count_primes(3) # 2, 3
    2
    >>> count_primes(4) # 2, 3
    2
    >>> count_primes(5) # 2, 3, 5
    3
    >>> count_primes(20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def count(n):
        s = 0
        for i in range(1, n+1):
            if condition(n, i):
                s += 1
        return s
    return count

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def cycle1(n):
        def cycle2(x):
            if n == 0:
                return x
            elif n % 3 == 1:
                return f1(cycle1(n-1)(x))
            elif n % 3 == 2:
                return f2(cycle1(n-1)(x))
            elif n % 3 == 0 :
                return f3(cycle1(n-1)(x))
        return cycle2
    return cycle1

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    up = n -1
    right = m - 1
    return factorial(up+right) // (factorial(up) * factorial(right))

def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x-1)
