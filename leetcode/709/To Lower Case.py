"""To Lower Case
Implement function ToLowerCase() that has a string parameter str,
and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""
import doctest


class Solution:
    def toLowerCase(self, ss):
        """
        :type str: str
        :rtype: str

        Examples:

            >>> s = Solution()
            >>> ss = 'Hello'
            >>> s.toLowerCase(ss)
            'hello'

            >>> ss = 'LOVELY'
            >>> s.toLowerCase(ss)
            'lovely'
        """
        left, right = 0, len(ss) - 1
        result = ''
        while left <= right:
            result += ss[left].lower()
            left += 1
        return result


if __name__ == "__main__":
    doctest.testmod(verbose=True)
