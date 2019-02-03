"""Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
"""
import doctest


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        Examples

            >>> s = Solution()
            >>> nums, k = [1, 2, 3, 1], 3
            >>> s.containsNearbyDuplicate(nums, k)
            True

            >>> nums, k = [1, 0, 1, 1], 1
            >>> s.containsNearbyDuplicate(nums, k)
            True

            >>> nums, k = [1, 2, 3, 1, 2, 3], 2
            >>> s.containsNearbyDuplicate(nums, k)
            False
        """
        occurrences = {}
        cursor = 0
        while cursor < len(nums):
            if nums[cursor] in occurrences:
                if ((cursor - occurrences.get(nums[cursor])) ** 2 <= k ** 2):
                    return True
            occurrences[nums[cursor]] = cursor
            cursor += 1
        return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
