#!/usr/bin/env python3
"""
Given the array of integers nums, you will choose two different indices i and
j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

    Input: nums = [3,4,5,2]
    Output: 12

Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will
get the maximum value, that is,
(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:

    Input: nums = [1,5,4,5]
    Output: 16

Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get
the maximum value of (5-1)*(5-1) = 16.

Example 3:

    Input: nums = [3,7]
    Output: 12


Constraints:

    - 2 <= nums.length <= 500
    - 1 <= nums[i] <= 10^3

"""
import unittest
from typing import List


class IterativeSolution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value, minor_value = nums[0], nums[1]
        index = 2
        nums_length = len(nums)

        if max_value < minor_value:
            max_value, minor_value = minor_value, max_value

        while index < nums_length:
            if nums[index] >= max_value:
                minor_value, max_value = max_value, nums[index]
            elif nums[index] >= minor_value:
                minor_value = nums[index]
            index += 1
        return minor_value * max_value - minor_value - max_value + 1


class SimpleSolution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[-1] - nums[-2] + 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s1 = IterativeSolution()
        self.s2 = SimpleSolution()

    def test_maxProduct(self):

        nums = [3, 4, 5, 2]
        self.assertEqual(self.s1.maxProduct(nums), self.s2.maxProduct(nums))

        nums = [1, 5, 4, 5]
        self.assertEqual(self.s1.maxProduct(nums), self.s2.maxProduct(nums))

        nums = [3, 7]
        self.assertEqual(self.s1.maxProduct(nums), self.s2.maxProduct(nums))

        nums = [9, 2, 8, 7, 8, 4, 5, 4, 5]
        self.assertEqual(self.s1.maxProduct(nums), self.s2.maxProduct(nums))

        nums = [10, 8, 1, 2, 3, 4, 5, 9, 8, 10]
        self.assertEqual(self.s1.maxProduct(nums), self.s2.maxProduct(nums))

        nums = [1, 2, 3, 4, 8, 9, 8, 4, 3, 2, 1]
        self.assertEqual(self.s1.maxProduct(nums), self.s2.maxProduct(nums))

if __name__ == "__main__":
    unittest.main()

