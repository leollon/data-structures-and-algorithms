#!/usr/bin/python3
"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

    Input: 2.00000, 10
    Output: 1024.00000

Example 2:

    Input: 2.10000, 3
    Output: 9.26100

Example 3:

    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]

Reference:

    https://zh.wikipedia.org/wiki/%E5%B9%B3%E6%96%B9%E6%B1%82%E5%B9%82#%E5%9F%BA%E6%9C%AC%E6%96%B9%E6%B3%95
"""


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Examples:

            >>> s = Solution()
            >>> x, n = 2.00000, 2
            >>> s.myPow(x, n)
            4.0
            >>> x, n = 2.10000, 3
            >>> s.myPow(x, n)
            9.261
            >>> x, n = 2.00000, -2
            >>> s.myPow(x, n)
            0.25
            >>> x, n = -100, -2
            >>> s.myPow(x, n)
            0.0001
            >>> x, n = 1.00001, 123456
            >>> s.myPow(x, n)
            3.43684
            >>> x, n = 2.00000, -2147483648
            >>> s.myPow(x, n)
            0.0
        """
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0: return 1
        if n > 2**31: return 0
        y = 1.0
        while n > 1:
            if n % 2 != 0:
                y = x * y
                x = x * x
                n = (n - 1) // 2
            else:
                x = x * x
                n = n // 2
        return int(x * y * 100000) / 100000


if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    s = Solution()
    x, n = 2.00000, -2147483648
    result = s.myPow(x, n)
    print(result)