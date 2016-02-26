from utils import *

# Q1
from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    city1_x = get_lat(city1)
    city1_y = get_lon(city1)

    city2_x = get_lat(city2)
    city2_y = get_lon(city2)

    return sqrt((city1_x - city2_x)**2 + (city1_y - city2_y) ** 2)

# Q2
def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    dis_2_ct1 = sqrt((lat - get_lat(city1)) ** 2 + (lon - get_lon(city1)) ** 2)
    dis_2_ct2 = sqrt((lat - get_lat(city2)) ** 2 + (lon - get_lon(city2)) ** 2)
    if dis_2_ct2 > dis_2_ct1:
        return get_name(city1)
    elif dis_2_ct2 < dis_2_ct1:
        return get_name(city2)
    else:
        return "same distance for either city"
# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    return a * b + c

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    divisor = n - 1
    def is_prime_helper(n, divisor):
        if divisor == 1:
            return True
        if n % divisor == 0:
            return False
        else:
            return is_prime_helper(n, divisor - 1)

    return is_prime_helper(n, divisor)
# Q5
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """

    if n == 1:
        return odd_term(1)
    elif n % 2 ==0:
        sum_ = even_term(n)
    else:
        sum_ = odd_term(n)

    return sum_ + interleaved_sum(n-1, odd_term, even_term)
