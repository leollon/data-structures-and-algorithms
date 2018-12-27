#!/usr/bin/python3
"""Given a sorted array nums, remove the duplicates in-place such that
duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums
being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification
to the input array will be known to the caller as well.

Internally you can think of this:

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples:

            >>> s = Solution()
            >>> nums = [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6]
            >>> result = s.removeDuplicates(nums)
            >>> nums[:result]
            [0, 1, 1, 2, 2, 3, 3, 4, 5, 6]
            >>> nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6]
            >>> result = s.removeDuplicates(nums)
            >>> nums[:result]
            [1, 1, 2, 2, 3, 3, 4, 5, 6]
        """
        if len(nums) <= 2:
            # 题目说允许元素最多允许出现次数是两次，所以数组长度小于等于2的时候，
            # 数组中元素不管是否重复，都可以立即返回
            return len(nums)
        duplicated_end, different_beg = 2, 2
        while different_beg < len(nums):
            if nums[duplicated_end - 2] != nums[different_beg]:
                # 因为允许元素最多重复两次，可以假设头两个元素是重复的，从第三个元素开始
                # 判断是否和元素开始重复的地方是否相等，如果不相等，则使用不相等的元素替换
                # 后续多余的元素
                nums[duplicated_end] = nums[different_beg]
                duplicated_end += 1
            different_beg += 1 # 查找不相等元素开始的地方
        return duplicated_end


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
