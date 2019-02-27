"""
Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space
complexity analysis.)
"""
import doctest


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Examples

            >>> s = Solution()
            >>> nums = [7, 1, 3, 5, 6, 4]
            >>> s.productExceptSelf(nums)
            [360, 2520, 840, 504, 420, 630]

            >>> nums = [1, 2, 3, 4]
            >>> s.productExceptSelf(nums)
            [24, 12, 8, 6]
        """
        n = len(nums)
        result = [1] * n
        left, cursor = 1, 0
        while cursor < n:
            result[cursor] = left
            left *= nums[cursor]
            cursor += 1
        right = 1
        cursor -= 1 # go back to tail index
        while cursor >= 0:
            result[cursor] *= right
            right *= nums[cursor]
            cursor -= 1
        return result


if __name__ == "__main__":
    doctest.testmod(verbose=True)
