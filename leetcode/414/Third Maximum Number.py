#!/usr/bin/python3
"""Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this
array. If it does not exist, return the maximum number. The time complexity
must be in O(n).

Example 1:
    Input: [3, 2, 1]

    Output: 1

    Explanation: The third maximum is 1.

Example 2:

    Input: [1, 2]

    Output: 2

    Explanation: The third maximum does not exist, so the maximum (2) is
                returned instead.

Example 3:
    Input: [2, 2, 3, 1]

    Output: 1

Explanation: Note that the third maximum here means the third maximum distinct
number.
Both numbers with value 2 are both considered as second maximum.
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples:
        
            >>> s = Solution()
            >>> nums = [1, 2]
            >>> s.thirdMax(nums)
            2
            >>> nums = [2, 2, 3, 1]
            >>> s.thirdMax(nums)
            1
            >>> nums = [2, 2, 2, 1]
            >>> s.thirdMax(nums)
            2
            >>> nums = [3, 2, 1]
            >>> s.thirdMax(nums)
            1
            >>> nums = [1, 3, 4, 5]
            >>> s.thirdMax(nums)
            3
            >>> nums = []
            >>> s.thirdMax(nums)

            >>> nums = [3]
            >>> s.thirdMax(nums)
            3
            """
        results = [None, None, None]
        for num in nums:
            if num in results: continue
            if not results[0] or num > results[0]:
                results[0], results[1], results[2] = num, results[0], results[1]
            elif not results[1] or num > results[1]:
                results[1], results[2] = num, results[1]
            elif not results[2] or num > results[2]:
                results[2] = num
        if results[-1] is None:
            return min(results)
        else:
            return results[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
