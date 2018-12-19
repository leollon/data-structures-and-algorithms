#!/usr/bin/python3
"""3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note:
The solution set must not contain duplicate triplets.

Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Examples:

            >>> s = Solution()
            >>> nums = [-1, 0, 1, 2, -1, -4]
            >>> s.threeSum(nums)
            [[-1, 0, 1], [-1, -1, 2]]
            >>> nums = [-1, 1]
            >>> s.threeSum(nums)
            []
            >>> nums = [-1, 2]
            >>> s.threeSum(nums)
            []
            >>> nums = []
            >>> s.threeSum(nums)
            []
            >>> nums = [-2, -7, -11, -8, 9, -7, -8, -15, 10, 4, 3, 9, 8,
            ...     11, 1, 12, -6, -14, -2, -1, -7, -13, -11, -15, 11, -2, 7,
            ...     -4, 12, 7, -3, -5, 7, -7, 3, 2, 1, 10, 2, -12, -1, 12, 12,
            ...     -8, 9, -9, 11, 10, 14, -6, -6, -8, -3, -2, 14, -15, 3, -2,
            ...     -4, 1, -9, 8, 11,5, -14, -1, 14, -6, -14, 2, -2, -8, -9,
            ...     -13, 0, 7, -7, -4, 2, -8, -2, 11, -9, 2, -13, -10, 2, 5, 4,
            ...     13, 13, 2, -1, 10, 14, -8, -14, 14,2,10
            ... ]
            >>> s.threeSum(nums)
            
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                target = 0 - nums[i] - nums[j]
                is_exist = self.binary_search(nums[j + 1:], target)
                if is_exist:
                    sub_array = [nums[i], nums[j], target]
                    if sub_array not in result:
                        result.append([nums[i], nums[j], target])

        return result

    def binary_search(self, array, target):
        low, height = 0, len(array) - 1
        while low <= height:
            mid = low + (height - low) // 2
            if array[mid] > target:
                height = mid - 1
            elif array[mid] < target:
                low = mid + 1
            else:
                return True
        return False


if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    from datetime import datetime
    s = Solution()
    nums = [
        -2, -7, -11, -8, 9, -7, -8, -15, 10, 4, 3, 9, 8, 11, 1, 12, -6, -14,
        -2, -1, -7, -13, -11, -15, 11, -2, 7, -4, 12, 7, -3, -5, 7, -7, 3, 2,
        1, 10, 2, -12, -1, 12, 12, -8, 9, -9, 11, 10, 14, -6, -6, -8, -3, -2,
        14, -15, 3, -2, -4, 1, -9, 8, 11, 5, -14, -1, 14, -6, -14, 2, -2, -8,
        -9, -13, 0, 7, -7, -4, 2, -8, -2, 11, -9, 2, -13, -10, 2, 5, 4, 13, 13,
        2, -1, 10, 14, -8, -14, 14, 2, 10
    ]
    start = datetime.now().timestamp()
    result = s.threeSum(nums)
    end = datetime.now().timestamp()
    print(result, len(result), len(nums), end - start)