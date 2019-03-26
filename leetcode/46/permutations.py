"""Permutations

"""
from itertools import permutations


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Example
            >>> s = Solution()
            >>> nums = [1]
            >>> s.permute(nums)
            [(1,)]

            >>> nums = [1, 2]
            >>> s.permute(nums)
            [(1, 2), (2, 1)]

            >>> nums = [1, 2, 3]
            >>> s.permute(nums)
            [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

            >>> nums = [1, 2, 3, 4]
            >>> s.permute(nums)
            [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]
        """
        return list(permutations(nums))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
