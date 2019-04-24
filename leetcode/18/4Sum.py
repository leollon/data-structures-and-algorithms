"""4Sum
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

    Example:

    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
    [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
    ]
"""
import bisect
import random


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]

        Examples

            >>> s = Solution()
            >>> nums, target = [1, 0, -1, 0, -2, 2], 0
            >>> s.fourSum(nums, target)
            [[-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]]
        """
        nums.sort()
        length = len(nums)
        result = []
        left = 0
        while left < length - 3:
            mid1 = left + 1
            while mid1 < length - 2:
                mid2 = mid1 + 1
                right = length - 1
                while mid2 < right:
                    if (nums[left] + nums[mid1] + nums[mid2] + nums[right]) > target:
                        right -= 1
                    elif (nums[left] + nums[mid1] + nums[mid2] + nums[right]) < target:
                        mid2 += 1
                    else:
                        result.append(
                            (nums[left], nums[mid1], nums[mid2], nums[right]))
                        mid2 += 1
                        right -= 1
                mid1 += 1
            left += 1
        return list(set(result))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
