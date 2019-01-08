#!/usr/bin/python3
"""Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
    Could you solve it in linear time?
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        """Sliding Window Maximum


        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Examples

        >>> nums, k = [1,3,-1,-3,5,3,6,7], 3
        >>> Solution().maxSlidingWindow(nums, k)
        [3, 3, 5, 5, 6, 7]

        >>> nums, k = [1,2, 3, 4, 5], 1
        >>> Solution().maxSlidingWindow(nums, k)
        [1, 2, 3, 4, 5]

        >>> nums, k = [2, 2, 3, 4, 5, 6], 4
        >>> Solution().maxSlidingWindow(nums, k)
        [4, 5, 6]

        >>> nums, k = [], 0
        >>> Solution().maxSlidingWindow(nums, k)
        []

        >>> nums, k = [1], 1
        >>> Solution().maxSlidingWindow(nums, k)
        [1]

        >>> nums, k = [1], 2
        >>> Solution().maxSlidingWindow(nums, k)
        []

        >>> nums, k = [1, 2, 3, 4, 5, 6, 7, 8, 9], 9
        >>> Solution().maxSlidingWindow(nums, k)
        [9]

        """
        if not nums or k > len(nums): return []
        result = []
        left = 0
        while (left + k) <= len(nums):
            result.append(max(nums[left:left+k]))
            left += 1
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
