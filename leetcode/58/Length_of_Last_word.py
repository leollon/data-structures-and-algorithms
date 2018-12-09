"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:

Input: "Hello World"
Output: 5
"""

import doctest 


class Solution1:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        Examples:
            >>> s = Solution1()
            >>> string = "hello world"
            >>> s.lengthOfLastWord(string)
            5
            >>> string = "Hello World"
            >>> s.lengthOfLastWord(string)
            5
            >>> string = "Hello World     "
            >>> s.lengthOfLastWord(string)
            5
            >>> string = "     H     ello      W     orld     "
            >>> s.lengthOfLastWord(string)
            4
            >>> string = ""
            >>> s.lengthOfLastWord(string)
            0
            >>> string = "Today is a nice day"
            >>> s.lengthOfLastWord(string)
            3
        """
        if not s:
            return 0
        word_list = s.strip().split(' ')
        if word_list:
            return len(word_list[-1])
        else:
            return 0


class Solution2:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        >>> s = Solution2()
        >>> string = "hello world"
        >>> s.lengthOfLastWord(string)
        5
        >>> string = "Hello World"
        >>> s.lengthOfLastWord(string)
        5
        >>> string = "Hello World     "
        >>> s.lengthOfLastWord(string)
        5
        >>> string = "     H     ello      W     orld     "
        >>> s.lengthOfLastWord(string)
        4
        >>> string = ""
        >>> s.lengthOfLastWord(string)
        0
        >>> string = "Today is a nice day"
        >>> s.lengthOfLastWord(string)
        3
        """
        if not s:
            return 0
        lamb = lambda x: x.isalpha()
        lst = s.split(' ')
        word_list = list(filter(lamb, lst))
        if word_list:
            return len(word_list[-1])
        else:
            return 0

if __name__ == "__main__":
    doctest.testmod(verbose=True)