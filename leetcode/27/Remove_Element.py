"""
Given an array nums and a value val, remove all instances of that value
in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums
being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums
containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification
to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

import doctest

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        Examples:
            >>> s = Solution()
            >>> nums, val = [3, 2, 2, 3], 3
            >>> s.removeElement(nums, val)
            2
            >>> nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
            >>> s.removeElement(nums, val)
            5
            >>> nums, val = [0, 1, 1, 2, 2, 3, 3], 3
            >>> s.removeElement(nums, val)
            5
            >>> nums, val = [2, 2, 2, 2], 2
            >>> s.removeElement(nums, val)
            0
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # nums.remove(nums[left]) # 方法1 O(n-1)
                
                # 方法一：边遍历边比对数组中的值与要从数组中移除的值，相同则移除，
                # 同时，将右边的指针往左边移动，如果不同左边指针向右边移动。为什么
                # right - 1，因为从原数组中移除该之后，数组的长度会变了。
                # 可以看得出这个方法暴力了些。

                nums[left] = nums[right]  # 方法2  O(n-1), O(1) extra memory

                # 方法二： 还是遍历并且对比，但是是使用后面的值赋值覆盖要移除的值。
                # 左边指针停下并等于右边指针的时候，也就是已经移除了要从数组中要移除的值了。
                # right - 1, 不断地使用后面的值进行赋值覆盖。
                right -= 1
            else:
                left += 1
        return left

if __name__ == "__main__":
    doctest.testmod(verbose=True)
