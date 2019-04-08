"""Find Pivot Index
Given an array of integers nums, write a method that returns the "pivot" index
of this array.

We define the pivot index as the index where the sum of the numbers to the left
of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1.
If there are multiple pivot indexes, you should return the left-most pivot
index.

Example 1:

    Input: 
    nums = [1, 7, 3, 6, 5, 6]
    Output: 3
    Explanation: 
    The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
    Also, 3 is the first index where this occurs.
 

Example 2:

    Input: 
    nums = [1, 2, 3]
    Output: -1
    Explanation: 
    There is no index that satisfies the conditions in the problem statement.
 

Note:

    The length of nums will be in the range [0, 10000].
    Each element nums[i] will be an integer in the range [-1000, 1000].

"""


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples

            >>> s = Solution()
            >>> nums = [1, 7, 3, 6, 5, 6]
            >>> s.pivotIndex(nums)
            3

            >>> nums = [-1, -1, -1, 0, 1, 1]
            >>> s.pivotIndex(nums)
            0

            >>> nums = [1, 1, 1, 1, 1, 5]
            >>> s.pivotIndex(nums)
            -1

            >>> nums = [1, 2, 1]
            >>> s.pivotIndex(nums)
            1

            >>> nums = [1, 2, 3]
            >>> s.pivotIndex(nums)
            -1

            >>> nums = []
            >>> s.pivotIndex(nums)
            -1

            >>> nums = [1, 2, 3, 0, 3, 2, 1]
            >>> s.pivotIndex(nums)
            3

            >>> nums = [1, 1, 1, 1, 1, 1, 1, 6]
            >>> s.pivotIndex(nums)
            6

            >>> nums = [3, 4, 7, 1, 2, 3, 1]
            >>> s.pivotIndex(nums)
            2

        """
        left_sum = 0
        total = sum(nums)
        pivot_index = -1
        for index, val in enumerate(nums):
            if left_sum == total - val - left_sum:
                pivot_index = index
                break
            left_sum += val
        return pivot_index


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
