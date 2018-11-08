"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

import doctest


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        >>> s = Solution()
        >>> a, b = "100", "11"
        >>> s.addBinary(a, b)
        '111'
        >>> a, b = "100", "1"
        >>> s.addBinary(a, b)
        '101'
        >>> a, b = "111", "11"
        >>> s.addBinary(a, b)
        '1010'
        >>> a, b = "110", "101"
        >>> s.addBinary(a, b)
        '1011'
        >>> a, b = "111", "111"
        >>> s.addBinary(a, b)
        '1110'
        >>> a, b = bin(15**2)[2:], bin(10**9)[2:]
        >>> s.addBinary(a, b)
        '111011100110101100101011100001'
        >>> a, b = bin(15**2)[2:], bin(10**9)[2:]
        >>> s.addBinary(a, b)
        '111011100110101100101011100001'
        """
        return bin(int(a, base=2) + int(b, base=2))[2:]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
