"""Implement strStr()
Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string?
This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().
"""
import doctest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        Examples

            >>> s = Solution()
            >>> haystack, needle = "hello", "ll"
            >>> s.strStr(haystack, needle)
            2

            >>> haystack, needle = "hello", ""
            >>> s.strStr(haystack, needle)
            0

            >>> haystack, needle = "", " "
            >>> s.strStr(haystack, needle)
            -1

            >>> haystack, needle = " ", ""
            >>> s.strStr(haystack, needle)
            0
        """
        if not needle: return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1


if __name__ == "__main__":
    doctest.testmod(verbose=True)
