"""Single Number
Given a non-empty array of integers, every element appears twice except for
one. Find that single one.

Note:

    Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Example 1:

    Input: [2,2,1]
    Output: 1

Example 2:

    Input: [4,1,2,1,2]
    Output: 4
"""
import doctest


class Solution:
    def singleNumber(self, nums):
        """
        :type n: List[int]
        :rtype: int

        Examples

            >>> s = Solution()
            >>> nums = [2, 2, 1]
            >>> s.singleNumber(nums)
            1

            >>> nums = [4, 1, 2, 1, 2]
            >>> s.singleNumber(nums)
            4
        """
        index = 0
        for num in nums:
            if nums.count(num) == 1:
                return num
        return 0


if __name__ == "__main__":
    doctest.testmod(verbose=True)
