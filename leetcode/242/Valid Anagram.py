#!/usr/bin/python3
"""
Given two strings s and t , write a function to determine
if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? How would you adapt your
    solution to such case?
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        >>> sol = Solution()
        >>> s, t = "anagram", "nagaram"
        >>> sol.isAnagram(s, t)
        True
        >>> s, t = "你好", "好你"
        >>> sol.isAnagram(s, t)
        True
        >>> s, t = "rat", "car"
        >>> sol.isAnagram(s, t)
        False
        """
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
