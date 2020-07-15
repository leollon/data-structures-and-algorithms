#!/usr/bin/env python3
"""

"""
import unittest
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, val in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if val == nums[j]:
                    count += 1
        return count


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_numIdenticalPairs(self):
        nums = [1, 2, 3, 1, 1, 3]
        self.assertEqual(4, self.solution.numIdenticalPairs(nums))

        nums = [1, 1, 1, 1]
        self.assertEqual(6, self.solution.numIdenticalPairs(nums))

        nums = [1, 2, 3]
        self.assertEqual(0, self.solution.numIdenticalPairs(nums))


if __name__ == "__main__":
    unittest.main()
