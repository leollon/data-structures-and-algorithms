#!/usr/bin/python3
"""Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution1:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Examples

            >>> nums, target = [5, 7, 7, 8, 8, 10], 8
            >>> Solution1().searchRange(nums, target)
            [3, 4]
            >>> nums, target = [5, 7, 8, 8, 8, 8, 8], 8
            >>> Solution1().searchRange(nums, target)
            [2, 6]
            >>> nums, target = [8, 8, 8, 8, 8, 8, 8, 8], 8
            >>> Solution1().searchRange(nums, target)
            [0, 7]
            >>> nums, target = [1, 2, 8, 8, 8, 8, 9, 10], 8
            >>> Solution1().searchRange(nums, target)
            [2, 5]
            >>> nums, target = [5, 7, 7, 8, 8, 10], 6
            >>> Solution1().searchRange(nums, target)
            [-1, -1]
            >>> nums, target = [1, 2, 3, 4, 8, 9, 10], 8
            >>> Solution1().searchRange(nums, target)
            [4, 4]
            >>> nums, target = [5, 6, 8, 9, 10, 11, 12], 8
            >>> Solution1().searchRange(nums, target)
            [2, 2]
            >>> nums, target = [], 8
            >>> Solution1().searchRange(nums, target)
            [-1, -1]
            >>> nums, target = [1], 8
            >>> Solution1().searchRange(nums, target)
            [-1, -1]
            >>> nums, target = [8], 8
            >>> Solution1().searchRange(nums, target)
            [0, 0]
            >>> nums, target = [2, 2], 1
            >>> Solution1().searchRange(nums, target)
            [-1, -1]
        """
        low, height = 0, len(nums) - 1
        found = False
        while len(nums):
            if len(nums) == 1 and nums[0] != target:
                low = height = -1
                break
            mid = low + (height - low) // 2
            if nums[mid] > target:
                    height = mid - 1
            elif nums[mid] < target:
                    low = mid + 1
            else:
                found = True
                if nums[low] != target:
                    low += 1
                if nums[height] != target:
                    height -= 1
            if found and nums[low] == nums[height] and nums[low] == target:
                return [low, height]
            if low > height: break
        if not len(nums) or low == height or not found: low = height = -1
        return [low, height]


class Solution2:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Examples

            >>> nums, target = [5, 7, 7, 8, 8, 10], 8
            >>> Solution2().searchRange(nums, target)
            [3, 4]
            >>> nums, target = [5, 7, 8, 8, 8, 8, 8], 8
            >>> Solution2().searchRange(nums, target)
            [2, 6]
            >>> nums, target = [8, 8, 8, 8, 8, 8, 8, 8], 8
            >>> Solution2().searchRange(nums, target)
            [0, 7]
            >>> nums, target = [1, 2, 8, 8, 8, 8, 9, 10], 8
            >>> Solution2().searchRange(nums, target)
            [2, 5]
            >>> nums, target = [5, 7, 7, 8, 8, 10], 6
            >>> Solution2().searchRange(nums, target)
            [-1, -1]
            >>> nums, target = [1, 2, 3, 4, 8, 9, 10], 8
            >>> Solution2().searchRange(nums, target)
            [4, 4]
            >>> nums, target = [5, 6, 8, 9, 10, 11, 12], 8
            >>> Solution2().searchRange(nums, target)
            [2, 2]
            >>> nums, target = [], 8
            >>> Solution2().searchRange(nums, target)
            [-1, -1]
            >>> nums, target = [1], 8
            >>> Solution2().searchRange(nums, target)
            [-1, -1]
            >>> nums, target = [8], 8
            >>> Solution2().searchRange(nums, target)
            [0, 0]
            >>> nums, target = [2, 2], 1
            >>> Solution2().searchRange(nums, target)
            [-1, -1]
        """
        if len(nums) == 0: return [-1, -1]
        count = nums.count(target)
        if count:
            if count == 1:
                return [nums.index(target), nums.index(target)]
            else:
                return [nums.index(target), nums.index(target) + count - 1]
        else:
            return [-1, -1]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
