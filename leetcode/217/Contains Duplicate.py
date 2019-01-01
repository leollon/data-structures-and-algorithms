#!/usr/bin/python3
"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution1:
    def containsDuplicate(self, nums):
        """
        Use one of the features of set, which is uniqueness in set, then
        check if its length is different to the length of list.

        :type nums: List[int]
        :rtype: bool

        Examples

            >>> s = Solution1()
            >>> nums = [1, 2, 3, 1]
            >>> s.containsDuplicate(nums)
            True

            >>> nums = [1, 2, 3, 4]
            >>> s.containsDuplicate(nums)
            False
            >>> nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
            >>> s.containsDuplicate(nums)
            True
        """
        if len(set(nums)) < len(nums): return True
        return False


class Solution2:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Examples

            >>> s = Solution2()
            >>> nums = [1, 2, 3, 1]
            >>> s.containsDuplicate(nums)
            True

            >>> nums = [1, 2, 3, 4]
            >>> s.containsDuplicate(nums)
            False
            >>> nums = [1,1,1,3,3,4,3,2,4,2]
            >>> s.containsDuplicate(nums)
            True
        """
        if len(self.removeDuplicate(nums)) == len(nums): return False
        return True

    def removeDuplicate(self, nums):
        # remove duplicates from sorted array
        nums.sort()
        first, second = 0, 1
        while second < len(nums):
            if nums[first] != nums[second]:
                first += 1
                nums[first] = nums[second]
            second += 1
        return nums[:first+1]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
