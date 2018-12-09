# coding: utf-8
# !/usr/bin/python3
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""
import doctest


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

        Examples:
            >>> s = Solution()
            >>> nums, target = [2,5,6,0,0,1,2], 0
            >>> s.search(nums, target)
            True
            >>> nums, target = [2,5,6,0,0,1,2], 3
            >>> s.search(nums, target)
            False
        """
        array = sorted(nums)
        low, height = 0, len(array) - 1
        exist = False
        while low <= height:
            mid = low + (height - low) // 2
            if array[mid] < target:
                low = mid + 1
            elif array[mid] > target:
                height = mid - 1
            else:
                exist = True
                break
        return exist

if __name__ == "__main__":
    doctest.testmod(verbose=True)
