"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    """数学概念
    对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。
    如果观察值有偶数个，则中位数不唯一，通常取最中间的两个数值的平均数作为中位数。
    计算有限个数的数据的中位数的方法是：把所有的同类数据按照大小的顺序排列。
    如果数据的个数是奇数，则中间那个数据就是这群数据的中位数；
    如果数据的个数是偶数，则中间那2个数据的算术平均值就是这群数据的中位数。
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        Examples:
            >>> s = Solution()
            >>> nums1, nums2 = [1, 3], [2, 4]
            >>> s.findMedianSortedArrays(nums1, nums2)
            2.5
            >>> nums1, nums2 = [1, 3], [2]
            >>> s.findMedianSortedArrays(nums1, nums2)
            2.0
            >>> nums1, nums2 = [1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]
            >>> s.findMedianSortedArrays(nums1, nums2)
            5.5
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 != 0:
            # 合并后的数组的数值个数是奇数
            return nums[len(nums)//2] / 1
        else:
            # 合并后的数组的数值个数是偶数
            return (nums[len(nums)//2] + nums[len(nums)// 2-1]) / 2


s = Solution()
nums1 = [1, 3]
nums2 = [2]

print(s.findMedianSortedArrays(nums1, nums2))