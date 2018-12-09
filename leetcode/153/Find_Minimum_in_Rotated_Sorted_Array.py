# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

    Input: [3,4,5,1,2] 
    Output: 1

Example 2:

    Input: [4,5,6,7,0,1,2]
    Output: 0

"""
import doctest


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples:
            >>> s = Solution()
            >>> nums = [3, 4, 5, 1, 2] 
            >>> s.findMin(nums)
            1
            >>> nums = [4, 8, 9, 10, 11, 0, 1, 2]
            >>> s.findMin(nums)
            0
            >>> nums = [2, 1]
            >>> s.findMin(nums)
            1
            >>> nums = [4, 5, 6, 1, 2, 3]
            >>> s.findMin(nums)
            1
            >>> nums = [1, 2]
            >>> s.findMin(nums)
            1
            >>> nums = [1]
            >>> s.findMin(nums)
            1
            >>> nums = []
            >>> s.findMin(nums)
        """
        if not len(nums): return None
        is_ascending = self.is_ascending(nums)
        target = nums[0]
        low, height = 1, len(nums) - 1
        while low <= height and not is_ascending:
            mid = low + (height - low) // 2
            if nums[mid] > target:
                low = mid + 1
            elif nums[mid] < target:
                height = mid - 1
                target = nums[mid]
        return target

    def is_ascending(self, nums):
        size = len(nums)
        is_ascending = True
        for i in range(len(nums) // 2):
            if nums[i] > nums[size - i - 1]:
                is_ascending = False
                break
        return is_ascending


if __name__ == "__main__":
    doctest.testmod(verbose=True)
