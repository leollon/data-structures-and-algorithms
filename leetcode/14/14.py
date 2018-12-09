# coding: utf-8
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

import doctest


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        Examples:
            >>> s = Solution()
            >>> strs = ["dog", "racecar", "car"]
            >>> s.longestCommonPrefix(strs)
            ''
            >>> strs = ["flower", "flow", "flight"]
            >>> s.longestCommonPrefix(strs)
            'fl'
            >>> strs = ["flower", "flow"]
            >>> s.longestCommonPrefix(strs)
            'flow'
            >>> strs = ["flower"]
            >>> s.longestCommonPrefix(strs)
            'flower'
            >>> strs = []
            >>> s.longestCommonPrefix(strs)
            ''
        """
        strs.sort(key=len) # 按长度排序，最短的排前面，用最短的字符串决定最长的字符串前缀
        if not len(strs): return ''
        first_str = strs.pop(0)
        length = len(first_str)
        idx = 0
        while idx != len(strs):
            if strs[idx][:length] == first_str[:length]:
                idx += 1 # 取字符串数组中的下一个字符串
                continue
            length -= 1  # 最长的字符串前缀长度变短
        return first_str[:length]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
