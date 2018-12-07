# coding: utf-8
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
import doctest


class Solution:
    def search_insert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> s = Solution()
        >>> nums, target = [1, 2, 3, 4, 5], 8
        >>> s.search_insert(nums, target)
        5
        >>> target = 0
        >>> s.search_insert(nums, target)
        0
        >>> target = 3
        >>> s.search_insert(nums, target)
        2
        >>> nums, target = [1], 1
        >>> s.search_insert(nums, target)
        0
        >>> nums, target = [], 1
        >>> s.search_insert(nums, target)
        0
        >>> nums, target = [2], 1
        >>> s.search_insert(nums, target)
        0
        >>> nums, target = [2], 3
        >>> s.search_insert(nums, target)
        1
        """
        nums.sort()
        return self.binary_search(nums, target)
        
    def binary_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type: int
        """
        low, height = 0, len(nums) - 1
        while low <= height:
            mid = low + (height - height) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                height = mid - 1
            else:
                break
        return low


if __name__ == "__main__":
    doctest.testmod(verbose=True)
