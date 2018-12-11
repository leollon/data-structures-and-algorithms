"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned.

Example 1:

    Input: 4
    Output: 2

Example 2:
    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

import doctest


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        >>> s = Solution()
        >>> x = 8
        >>> s.mySqrt(x)
        2
        >>> x = 4
        >>> s.mySqrt(x)
        2
        """
        if x <= 0: return 0
        err = 1e-15
        num = x
        while (abs(num - x/num) > err * num):
            num = (x/num + num) / 2.0
        return int(num)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
