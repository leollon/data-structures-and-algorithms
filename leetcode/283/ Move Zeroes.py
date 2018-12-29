#!/usr/bin/python3
"""Move zeroes
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        Examples:

            >>> s = Solution()
        >>> nums = [0, 1, 0, 3, 12]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]
        
        >>> nums = [0, 1, 0, 0, 3, 12]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0, 0]
        
        >>> nums = [0, 0, 0, 0, 1, 2]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 2, 0, 0, 0, 0]
        
        >>> nums = [1, 2, 3, 0, 0, 0, 0]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 2, 3, 0, 0, 0, 0]
        
        >>> nums = [0, 0, 0, 1, 0, 2, 3, 4, 0, 0, 0]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0]
        
        >>> nums = [1, 0, 1]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 1, 0]

        >>> nums = [0, 1]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 0]

        >>> nums = [0, 1, 0, 2, 0, 3, 0, 4]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 2, 3, 4, 0, 0, 0, 0]
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0:
                # 将左边数值为0和右边不等于0的数值进行交换
                if nums[right] != 0:
                    nums[right], nums[left] = nums[left], nums[right]
                else:
                    # 寻找第一个非0的数值
                    right += 1
                    continue
            left += 1
            right += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
