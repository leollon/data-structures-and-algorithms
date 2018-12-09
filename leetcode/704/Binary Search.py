# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
 

Note:
    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].
"""
import doctest


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Examples:

            >>> nums, target = [-1,0,3,5,9,12], 2
            >>> s = Solution()
            >>> s.search(nums, target)
            -1
            
            >>> nums, target = [-1,0,3,5,9,12], 3
            >>> s.search(nums, target)
            2

            >>> nums, target = [2, 3, 4, 5, 7, 9, 10], 1
            >>> s.search(nums, target)
            -1

        """
        return self.__binary_search(nums, target, 0, len(nums) - 1)
    
    def __binary_search(self, nums, target, low, height):
        if low > height: return -1
        mid = low + (height - low) // 2
        if nums[mid] > target:
            return self.__binary_search(nums, target, low, mid - 1)
        elif nums[mid] < target:
            return self.__binary_search(nums, target, mid + 1, height)
        else:
            return mid


if __name__ == "__main__":
    doctest.testmod(verbose=True)
