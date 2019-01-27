"""Decoded String at Index
An encoded string S is given.  To find and write the decoded string to a tape,
the encoded string is read one character at a time and the following steps are
taken:
    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit (say d), the entire current tape is
repeatedly written d-1 more times in total.

Now for some encoded string S, and an index K, find and return the K-th
letter(1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
 

Note:

    2 <= S.length <= 100
    S will only contain lowercase letters and digits 2 through 9.
    S starts with a letter.
    1 <= K <= 10^9
    The decoded string is guaranteed to have less than 2^63 letters.
"""
import doctest


class Solution:
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str

        Examples

        >>> s = Solution()
        >>> ss, k = "leet2code3", 10
        >>> s.decodeAtIndex(ss, k)
        'o'

        >>> ss, k = "2abc3", 3
        >>> s.decodeAtIndex(ss, k)
        'c'

        >>> ss, k = "ha22", 5
        >>> s.decodeAtIndex(ss, k)
        'h'

        >>> ss, k = "czjkk9elaqwiz7s6kgvl4gjixan3ky7jfdg3kyop3husw3fm289thisef8blt7a7zr5v5lhxqpntenvxnmlq7l34ay3jaayikjps", 768077956
        >>> s.decodeAtIndex(ss, k)
        'c'
        """
        length = 0
        # 先求编码完后的字符串的总长度，即length
        for ch in s:
            if ch.isdigit():
                length *= int(ch)
            else:
                length += 1
        for ch in reversed(s):
            # 翻转字符串，进行与编码后求总长度的相反运算，同时对k进行模运算
            k %= length
            if k == 0 and ch.isalpha():
                return ch
            if ch.isalpha():
                length -= 1
            else:
                length //= int(ch)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
