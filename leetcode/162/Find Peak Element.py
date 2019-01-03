#!/usr/bin/python3
"""Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
return its index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

    Input: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 
    Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:

Your solution should be in logarithmic complexity.
"""
import doctest


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples:
            >>> s = Solution()
            >>> nums = [1, 2, 1, 3, 5, 6, 4]
            >>> s.findPeakElement(nums)
            1
            >>> nums = [1, 2]
            >>> s.findPeakElement(nums)
            1
            >>> nums = [2, 1]
            >>> s.findPeakElement(nums)
            0
            >>> nums = []
            >>> s.findPeakElement(nums)
            
            >>> nums = [1]
            >>> s.findPeakElement(nums)
            0
            >>> nums = [3, 2, 1]
            >>> s.findPeakElement(nums)
            0
            >>> nums = [1, 3, 2, 4]
            >>> s.findPeakElement(nums)
            1
            >>> nums = [1, 2, 3, 4]
            >>> s.findPeakElement(nums)
            3
            >>> nums = [1, 2, 3]
            >>> s.findPeakElement(nums)
            2
        """
        if not nums: return None
        if len(nums) == 1: return 0
        j = 0
        while j < len(nums) - 1:
            if nums[j] > nums[j+1] and nums[j] > nums[j-1]:
                return j
            j += 1
        if j == len(nums) - 1:
            return len(nums) - 1


if __name__ == "__main__":
    doctest.testmod(verbose=True)
