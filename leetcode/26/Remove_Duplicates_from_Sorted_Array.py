"""
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums
being modified to 0, 1, 2, 3, and 4 respectively.

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

import doctest

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> nums = [1,1,2]
        >>> s.removeDuplicates(nums)
        2
        >>> nums
        [1, 2]
        >>> nums = [0,0,1,1,1,2,2,3,3,4]
        >>> s.removeDuplicates(nums)
        5
        >>> nums
        [0, 1, 2, 3, 4]
        """
        # 这里有一种双指针的意思在里面，此指针非比C语言中的指针范畴，这里的指针亦可称为箭头。
        if (not len(nums)):
            return 0
        left = 0
        right = 1
        while right < len(nums):  # O(len(nums))
            if nums[left] != nums[right]:
                # 左边的的指针走得慢，右边指针走得快的同时，利用右边的这个指针作为索引从数组中取值同
                # 走得慢的指针指向的值作比较，如果相同，右边的指针继续行进，直到找到不相等，此时使用
                # 以右边指针为起点指向的所有元素对左边后面的进行赋值覆盖，此时两个指针也同步向右移动。
                # 如果左边指针停下了，说明此时左指针为起点到结尾的的所有元素都是相同的。
                left += 1;
                nums[left] = nums[right] # O(1) extra memory
            right +=1
        del nums[left+1:]
        return (left + 1)

if __name__ == "__main__":
    doctest.testmod(verbose=True)