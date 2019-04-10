#!/usr/bin/python3
"""Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Follow up:

    A rather straight forward Solution is a two-pass algorithm using counting
    sort.
    First, iterate the array counting number of 0's, 1's, and 2's,
    then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?
"""


class Solution1:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        Examples:

            >>> s = Solution1()
            >>> nums = [2, 0, 2, 1, 1, 0]
            >>> s.sortColors(nums)
            >>> nums == sorted(nums)
            True
        """
        self.selectionSort(nums)

    def selectionSort(self, nums):
        for i in range(len(nums) - 1):
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            if min != i:
                nums[i], nums[min] = nums[min], nums[i]


class Solution2:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        Examples:

            >>> s = Solution1()
            >>> nums = [2, 0, 2, 1, 1, 0]
            >>> s.sortColors(nums)
            >>> nums == sorted(nums)
            True
        """
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot)
            self.quick_sort(nums, pivot + 1, right)

    def partition(self, nums, left, right):
        i, j = left + 1, right
        pivot = nums[left]
        while True:
            while i < right and nums[i] <= pivot:
                i += 1
            while j > left and nums[j] >= pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        if pivot >= nums[j]:
            nums[left], nums[j] = nums[j], nums[left]
        else:
            j -= 1
        return j


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
