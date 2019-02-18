"""Find Minimum in Rotated Sorted Array II
"""
import doctest


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples

            >>> s = Solution()
            >>> nums = [1, 3, 5]
            >>> s.findMin(nums)
            1
            
            >>> nums = [10, 1, 10, 10, 10]
            >>> s.findMin(nums)
            1

            >>> nums = [1]
            >>> s.findMin(nums)
            1

            >>> nums = [3, 3, 3, 1, 3]
            >>> s.findMin(nums)
            1
        """
        if not len(nums): return None
        target = nums[0]
        low, height = 0, len(nums) - 1
        while low <= height:
            mid = low + (height - low) // 2
            if nums[mid] > nums[height]:
                low = mid + 1
            elif nums[mid] < target:
                height = mid - 1
                target = nums[mid]
            else:
                height -= 1
        return target


if __name__ == "__main__":
    doctest.testmod(verbose=True)
