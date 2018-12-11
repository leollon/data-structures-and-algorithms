# coding: utf-8
#!/usr/bin/python3
"""Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:

    Input: "race a car"
    Output: false
"""
import doctest

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        >>> s = Solution()
        >>> str_val = "A man, a plan, a canal: Panama"
        >>> s.isPalindrome(str_val)
        True
        >>> str_val = "0P"
        >>> s.isPalindrome(str_val)
        False
        >>> str_val = "a"
        >>> s.isPalindrome(str_val)
        True
        >>> str_val = "race a car"
        >>> s.isPalindrome(str_val)
        False
        """
        is_palindrome = True
        if not s: return is_palindrome
        s = self.my_replace(s)
        low, height = 0, len(s) - 1
        while low < height:
            if s[low] != s[height]:
                is_palindrome = False
            low += 1
            height -= 1
        return is_palindrome
    
    def my_replace(self, s):
        new_str = ''
        for ch in s:
            if not ch.isalnum():
                continue
            new_str += ch.lower()
        return new_str


if __name__ == "__main__":
    doctest.testmod(verbose=True)
