"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

- Try to come up as many solutions as you can, there are at least 3 different
  ways to solve this problem.
- Could you do it in-place with O(1) extra space?
"""

import doctest


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        >>> s = Solution()
        >>> nums, k = [1,2,3,4,5,6,7], 3
        >>> s.rotate(nums, k)
        >>>
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]
        >>> nums, k = [-1,-100,3,99], 2
        >>> s.rotate(nums, k)
        >>>
        >>> nums
        [3, 99, -1, -100]
        """
        # O(n)
        while k:
            nums.insert(0, nums.pop()) # O(1) extra space
            k -= 1


if __name__ == '__main__':
    doctest.testmod(verbose=True)
