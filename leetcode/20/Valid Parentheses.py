#!/usr/bin/python3
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

    Input: "()"
    Output: true

Example 2:

    Input: "()[]{}"
    Output: true

Example 3:

    Input: "(]"
    Output: false

Example 4:

    Input: "([)]"
    Output: false

Example 5:

    Input: "{[]}"
    Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Examples:

            >>> s = Solution()
            >>> str_val = "{[]}"
            >>> s.isValid(str_val)
            True
            >>> str_val = "()"
            >>> s.isValid(str_val)
            True
            >>> str_val = "([)]"
            >>> s.isValid(str_val)
            False
            >>> str_val = ""
            >>> s.isValid(str_val)
            True
            >>> str_val = ")(){[]}"
            >>> s.isValid(str_val)
            False
            >>> str_val = "(("
            >>> s.isValid(str_val)
            False
            >>> str_val = "))"
            >>> s.isValid(str_val)
            False
            >>> str_val = "{[]"
            >>> s.isValid(str_val)
            False
            >>> str_val = "[])"
            >>> s.isValid(str_val)
            False
        """
        left = []
        is_valid = False
        if not len(s): is_valid = True
        for ch in s:
            if ch not in [')', '}', ']']:
                left.append(ch)
            elif (len(left) > 0):
                pair = left.pop()
                if (pair + ch) not in ['()', '{}', '[]']:
                    is_valid = False
                    break
                else:
                    is_valid = True
            else:
                is_valid = False
                break
        if len(left): is_valid = False
        return is_valid


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
