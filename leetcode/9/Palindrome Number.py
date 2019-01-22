"""Palindrome Number
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

    Coud you solve it without converting the integer to a string?
"""
import doctest


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        Examples:
            >>> s = Solution()
            >>> x = 121
            >>> s.isPalindrome(x)
            True
            >>> x = -121
            >>> s.isPalindrome(x)
            False
            >>> x = 369
            >>> s.isPalindrome(x)
            False
        """
        if x < 0: return False
        result = 0
        orig_x = x
        while x:
            result = (x % 10) + (result * 10)
            x = x // 10
        return (result == orig_x)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
