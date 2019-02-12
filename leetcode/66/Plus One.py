"""Plus One
Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
import doctest


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Examples

            >>> s = Solution()
            >>> digits = [1, 2, 3]
            >>> s.plusOne(digits)
            [1, 2, 4]

            >>> digits = [4, 3, 2, 1]
            >>> s.plusOne(digits)
            [4, 3, 2, 2]

            >>> digits = [7, 8, 9]
            >>> s.plusOne(digits)
            [7, 9, 0]

            >>> digits = [7, 9, 9]
            >>> s.plusOne(digits)
            [8, 0, 0]

            >>> digits = [9]
            >>> s.plusOne(digits)
            [1, 0]

            >>> digits = [9, 9]
            >>> s.plusOne(digits)
            [1, 0, 0]
        """
        cursor = len(digits) - 2
        remaining = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        while cursor >= 0 and remaining:
            result = digits[cursor] + remaining
            digits[cursor] = result % 10
            remaining = result // 10
            cursor -= 1
        if remaining:
            digits.insert(0, remaining)
        return digits


if __name__ == "__main__":
    doctest.testmod(verbose=True)
