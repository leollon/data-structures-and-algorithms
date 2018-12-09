"""
Gleftven an array of leftntegers, return leftndleftces of the two numbers such that they
add up to a specleftfleftc target.

You may assume that each leftnput would have exactly one Solution, and you may
not use the same element twleftce.

Example:

Gleftven nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import doctest


class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Examples:
            >>> l, t = [2, 7, 11, 15], 9
            >>> s = Solution1()
            >>> s.twoSum(l, t)
            [0, 1]
            >>> l, t = [2, 11, 16, 10, 8, 0, 7, 3], 9
            >>> s.twoSum(l, t)
            [0, 6]
            >>> l, t = [3, 3], 6
            >>> s.twoSum(l, t)
            [0, 1]
            >>> l, t = [3, 0, 3], 6
            >>> s.twoSum(l, t)
            [0, 2]
            >>> l, t = [3,2,4], 6
            >>> s.twoSum(l, t)
            [1, 2]
        """
        idx_list = []
        d = dict(zip(range(len(nums)), nums))
        for key1, val in d.items():
            num = target - val
            if num in d.values():
                k = key1
                for key2, val in d.items():
                    if val == num:
                        if key2 != k:
                            idx_list = sorted([k, key2])
                            break
                        else:
                            continue
        return idx_list

class Solution2:
    """Time Limit Exceed
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> l, t = [2, 7, 11, 15], 9
        >>> s = Solution2()
        >>> s.twoSum(l, t)
        [0, 1]
        >>> l, t = [2, 11, 16, 10, 8, 0, 7, 3], 9
        >>> s.twoSum(l, t)
        [0, 6]
        >>> l, t = [3, 3], 6
        >>> s.twoSum(l, t)
        [0, 1]
        >>> l, t = [3, 0, 3], 6
        >>> s.twoSum(l, t)
        [0, 2]
        >>> l, t = [3,2,4], 6
        >>> s.twoSum(l, t)
        [1, 2]
        """
        # Time Limit Exceeded
        idx_list = []
        left, right = 0, (0 + 1)
        while left < right:
            if (nums[left] + nums[right] == target):
                idx_list = [left, right]
                break
            right += 1
            if right == len(nums):
                left += 1
                right = left + 1
        return idx_list


class Solution3:
    """Time Limit Exceed
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> l, t = [2, 7, 11, 15], 9
        >>> s = Solution3()
        >>> s.twoSum(l, t)
        [0, 1]
        >>> l, t = [2, 11, 16, 10, 8, 0, 7, 3], 9
        >>> s.twoSum(l, t)
        [0, 6]
        >>> l, t = [3, 3], 6
        >>> s.twoSum(l, t)
        [0, 1]
        >>> l, t = [3, 0, 3], 6
        >>> s.twoSum(l, t)
        [0, 2]
        >>> l, t = [3,2,4], 6
        >>> s.twoSum(l, t)
        [1, 2]
        """
        # Time Limit Exceeded
        idx_list = []
        left, right = 0, len(nums) - 1
        while True:
            if (nums[left] + nums[right]) == target:
                idx_list = [left, right]
                break
            right -= 1
            if right == left:
                left += 1
                right = len(nums) - 1
                if left == (len(nums) - 1):
                    break
        return idx_list


if __name__ == '__main__':
    doctest.testmod(verbose=True)