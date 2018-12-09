"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space
(size that is greater or equal tom + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

import doctest


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        Examples:
            >>> s = Solution()
            >>> nums1, m = [1, 2, 3, 0, 0, 0], 3
            >>> nums2, n = [2, 5, 6], 3
            >>> s.merge(nums1, m, nums2, n)
            >>> nums1
            [1, 2, 2, 3, 5, 6]
            >>> nums1, n = [2, 5, 6, 0, 0, 0], 3
            >>> nums2, m = [1, 2, 3], 3
            >>> s.merge(nums1, m, nums2, n)
            >>> nums1
            [1, 2, 2, 3, 5, 6]
            >>> nums1, m= [2, 3, 3, 4, 0], 1
            >>> nums2, n = [1], 1
            >>> s.merge(nums1, m, nums2, n)
            >>> nums1
            [1, 2, 3, 3, 4]
            >>> nums1, m= [2, 3, 3, 4, 0], 1
            >>> nums2, n = [5], 1
            >>> s.merge(nums1, m, nums2, n)
            >>> nums1
            [2, 3, 3, 4, 5]
        """
        if not nums2:
            return
        if not nums1:
            nums1 = nums2
            return
        del nums1[-n:]
        nums1.extend(nums2)
        nums1.sort()

if __name__ == "__main__":
    doctest.testmod(verbose=True)
