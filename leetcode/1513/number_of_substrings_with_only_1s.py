#!/usr/bin/env python3
"""
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

    Input: s = "0110111"
    Output: 9
    Explanation: There are 9 substring in total with only 1's characters.
    "1" -> 5 times.
    "11" -> 3 times.
    "111" -> 1 time.
Example 2:

    Input: s = "101"
    Output: 2
    Explanation: Substring "1" is shown 2 times in s.

Example 3:

    Input: s = "111111"
    Output: 21
    Explanation: Each substring contains only 1's characters.

Example 4:

    Input: s = "000"
    Output: 0


Constraints:

    - s[i] == '0' or s[i] == '1'
    - 1 <= s.length <= 10^5

Hint:
    Count number of 1s in each consecutive-1 group. For a group with n
    consecutive 1s, the total contribution of it to the final answer is
    (n + 1) * n // 2.
"""
import unittest


class Solution:
    def numSub(self, s: str) -> int:
        index = 0
        result = []
        count = 0

        while index < len(s):
            if s[index] == "0":
                result.append(count * (count + 1) // 2)
                count = 0
            else:
                count += 1
            index += 1
        result.append(count * (count + 1) // 2)
        return sum(result) % (10 ** 9 + 7)


class FasterSolution:
    def numSub(self, s: str) -> int:
        result = 0
        ones = s.split('0')  # one 1s substring and '' in the list

        for ss in ones:
            l = len(ss)
            result += l * (l + 1) // 2
        return result % (10 ** 9 + 7)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s_solution = Solution()
        self.f_solution = FasterSolution()

    def test_numSub(self):

        s = "0110111"
        self.assertEqual(self.f_solution.numSub(s), self.s_solution.numSub(s))

        s = "11111111111"
        self.assertEqual(self.f_solution.numSub(s), self.s_solution.numSub(s))

        s = "00000000000000"
        self.assertEqual(self.f_solution.numSub(s), self.s_solution.numSub(s))

        s = "1000000000000000"
        self.assertEqual(self.f_solution.numSub(s), self.s_solution.numSub(s))

        s = "0101010101010101"
        self.assertEqual(self.f_solution.numSub(s), self.s_solution.numSub(s))

        s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        self.assertEqual(self.f_solution.numSub(s), self.s_solution.numSub(s))


if __name__ == "__main__":
    unittest.main()
