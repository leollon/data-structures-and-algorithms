#!/usr/bin/python3
"""First Unique Character in a String
Given a string, find the first non-repeating character in it
and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note:
    You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        Examples

            >>> s = "leetcode"
            >>> Solution().firstUniqChar(s)
            0
            >>> s = "loveleetcode"
            >>> Solution().firstUniqChar(s)
            2
            >>> s = "cc"
            >>> Solution().firstUniqChar(s)
            -1
            >>> s = "ccz"
            >>> Solution().firstUniqChar(s)
            2
        """
        ocurrence = set()
        for index in range(len(s)):
            if s[index] not in s[index+1:] and s[index] not in ocurrence:
                return index
            else:
                ocurrence.add(s[index])
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
