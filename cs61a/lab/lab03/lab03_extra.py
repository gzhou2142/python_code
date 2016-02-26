from lab03 import *
from math import *
# Q9
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y + [int(i) for i in str(n)][len(str(x))-1] * 10 ** (len(str(x)) - 1)
    while x > 0:
        x, y = x // 10, f()
    return y == n

# Q10
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def ten_pairs_helper(digit):
        return [int(i) for i in str(n)].count(digit)
    
    digits = [int(i) for i in str(n)]
    pairs = []
    for digit in digits:
        if digit == 5:
            pairs.append(ten_pairs_helper(5)*[5])
            for i in range(ten_pairs_helper(5)):
                digits.remove(5)
            
        if 10 - digit in digits and digit != 5:
            pairs.append(ten_pairs_helper(digit)*[digit] + ten_pairs_helper(10-digit)*[10-digit])
            for i in range(ten_pairs_helper(digit)):
                digits.remove(digit)
            for i in range(ten_pairs_helper(10 - digit)):
                digits.remove(10 - digit)
        
  

    num_ten_pairs = 0
    for n in pairs:
        if 5 in n:
            num_ten_pairs = factorial(len(n)-1)
        else:
            num_ten_pairs += n.count(n[0]) * n.count(10 - n[0])
            
    return num_ten_pairs

        
