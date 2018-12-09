"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.
"""

import doctest

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        Examples:

            >>> s = Solution()
            >>> x = 123
            >>> s.reverse(x)
            321
            >>> x = -123
            >>> s.reverse(x)
            -321
            >>> x = 120
            >>> s.reverse(x)
            21
        """
        ret_value = self.my_reverse(x)
        if not (-(2**31) <= ret_value <= (2**31-1)): return 0
        return ret_value
    
    def my_reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        sum = 0
        if x < 0:
            negative = True
            x = 0 - x
        while x:
            sum = (sum * 10) + (x % 10)
            x //= 10
        if negative:
            sum = 0 - sum
        return sum

if __name__ == "__main__":
    doctest.testmod(verbose=True)
