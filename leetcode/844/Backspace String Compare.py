"""Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
    Can you solve it in O(N) time and O(1) space?

"""
import doctest


class Solution:
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        """
        :type S: str
        :type T: str
        :rtype: bool

        Examples

            >>> s = Solution()
            >>> S, T = "ab#c", "ad#c"
            >>> s.backspaceCompare(S, T)
            True

            >>> S, T = "y#fo##f", "y#f#o##f"
            >>> s.backspaceCompare(S, T)
            True
        """
        s, t = [], []
        for ch in S:
            if ch == '#':
                if s:
                    s.pop()
            else:
                s.append(ch)
        for ch in T:
            if ch == '#':
                if t:
                    t.pop()
            else:
                t.append(ch)
        return ''.join(s) == ''.join(t)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
