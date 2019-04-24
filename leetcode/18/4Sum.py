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
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                k = j + 1
                while k < length:
                    rest = target - (nums[i] + nums[j] + nums[k])
                    index = bisect.bisect_left(nums, rest, k+1, length)
                    if index < length and nums[index] == rest:
                        result.append((nums[i], nums[j], nums[k], rest))
                    k += 1
                j += 1
            i += 1
        return list(set(result))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
