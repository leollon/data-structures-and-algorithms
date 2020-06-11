"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

    Input: [3,2,3]
    Output: [3]
Example 2:

    Input: [1,1,1,3,3,2,2,2]
    Output: [1,2]
"""
import doctest
from typing import List

class Solution:
    """
    >>> solution = Solution()
    >>> solution.majorityElement([1, 0])
    [0, 1]
    >>> solution.majorityElement([1,2,3])
    []
    >>> solution.majorityElement([1,2,3,3,3,3,3])
    [3]
    >>> solution.majorityElement([1,1])
    [1]
    >>> solution.majorityElement([1,0,1])
    [1]
    >>> solution.majorityElement([])
    []
    >>> solution.majorityElement([1])
    [1]
    >>> solution.majorityElement([3,2,3])
    [3]
    >>> solution.majorityElement([1,1,1,3,3,2,2,2])
    [1, 2]
    >>> solution.majorityElement([6,6,6,7,7])
    [6, 7]
    >>> solution.majorityElement([1,1,2,3,4,5,6,7,8,9,10])
    []
    >>> solution.majorityElement([2,3,4,5,6,7,8,9,9])
    []
    >>> solution.majorityElement([1,2,3,3,4,5,6,7,7,8,9])
    []
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0 or length == 1 or length == 2:
            return list(set(nums))
        nums.sort()
        slow, fast = 0, 1
        results = []
        while length > 2 and fast != length:
            if nums[fast] ^ nums[slow]:
                occurances = fast - slow
                if occurances > (length // 3):
                    # nums[fast] xor nums[slow], 0 if nums[fast] is equal to
                    # nums[slow]
                    results.append(nums[slow])
                slow = fast
            fast += 1
        if fast - slow > (length // 3):
            results.append(nums[slow])
        return results


if __name__ == "__main__":
    doctest.testmod(verbose=True)

