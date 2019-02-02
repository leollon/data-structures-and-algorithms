"""Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import doctest
import collections


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str

        Examples

            >>> s = Solution()
            >>> ss = "tree"
            >>> s.frequencySort(ss)
            'eetr'

            >>> ss = "cccaaa"
            >>> s.frequencySort(ss)
            'cccaaa'

            >>> ss = "Aabb"
            >>> s.frequencySort(ss)
            'bbAa'
        """
        result = ''
        data_map = collections.Counter(s)
        for (ch, times) in data_map.most_common():
            result += ch * times
        return result
        

if __name__ == "__main__":
    doctest.testmod(verbose=True)