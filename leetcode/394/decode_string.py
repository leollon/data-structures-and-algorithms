#!/usr/bin/env python3
import unittest


class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        digits = []
        result = ''
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                digits.append(num)
                str_stack.append(result)
                result = ""
                num = ""
            elif ch == "]":
                result = str_stack.pop() + int(digits.pop()) * result
            else:
                result += ch
        return result


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_decodeString(self):
        s = "3[a]2[bc]"
        self.assertEqual("aaabcbc", self.solution.decodeString(s))

        s = "3[a2[c]]"
        self.assertEqual("accaccacc", self.solution.decodeString(s))

        s = "2[abc]3[cd]ef"
        self.assertEqual("abcabccdcdcdef", self.solution.decodeString(s))

        s = "abc3[cd]xyz"
        self.assertEqual("abccdcdcdxyz", self.solution.decodeString(s))

        s = "1[3[4[b]qwe5[a]]]"
        self.assertEqual(
            "bbbbqweaaaaabbbbqweaaaaabbbbqweaaaaa",
            self.solution.decodeString(s))


if __name__ == "__main__":
    unittest.main()
