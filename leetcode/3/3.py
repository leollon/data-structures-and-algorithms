""" Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating
characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence
             and not a substring.
"""


class SolutionTLE:
    """TLE
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        beg, end = 0, 1
        length = len(s)
        if not s:
            return 0
        max_length = 1
        while beg != length - 1:
            substring = s[beg:end]
            distance = end - beg
            if len(set(substring)) == distance and distance > max_length:
                    max_length = distance
            if end == length:
                beg += 1
                end = beg
            end += 1
        return max_length

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        >>> s = Solution()
        >>> string = "b"
        >>> s.lengthOfLongestSubstring(string)
        1
        >>> string = "abcabcbb"
        >>> s.lengthOfLongestSubstring(string)
        3
        >>> string = "bbbbb"
        >>> s.lengthOfLongestSubstring(string)
        1
        >>> string = "pwwkew"
        >>> s.lengthOfLongestSubstring(string)
        3
        >>> string = "abcdedf"
        >>> s.lengthOfLongestSubstring(string)
        5
        >>> string = "bbbbbbdf"
        >>> s.lengthOfLongestSubstring(string)
        3
        >>> string = "abcdefg"
        >>> s.lengthOfLongestSubstring(string)
        7
        >>> string = "ohomm"
        >>> s.lengthOfLongestSubstring(string)
        3
        """
        length = len(s)
        if not length: return 0
        beg, end = 0, 0
        max_length = 1
        while beg < length and end < length:
            if s[end] not in s[beg:end]:
                end += 1
                max_length = max(max_length, end - beg)
            else:
                beg += 1
        return max_length


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
