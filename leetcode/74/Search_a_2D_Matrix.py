# coding: utf-8
# !/usr/bin/python3
"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
import doctest


class Solution:
    def search_matrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        >>> s = Solution()
        >>> matrix = [
        ...     [1,   3,  5,  7],
        ...     [10, 11, 16, 20],
        ...     [23, 30, 34, 50]
        ... ]
        >>> target = 3
        >>> s.search_matrix(matrix, target)
        True
        >>> target = 13
        >>> s.search_matrix(matrix, target)
        False
        >>> matrix, target = [[0]], 2
        >>> s.search_matrix(matrix, target)
        False
        >>> matrix, target = [[0]], 0
        >>> s.search_matrix(matrix, target)
        True
        >>> matrix, target = [[1], [3]], 3
        >>> s.search_matrix(matrix, target)
        True
        >>> matrix, target = [[1], [3]], 2
        >>> s.search_matrix(matrix, target)
        False
        """
        return self.target_exists(matrix, target)

    def target_exists(self, matrix, target):
        index = False
        for array in matrix:
            index = self.binary_search(array, target)
            if not index:
                continue
            else:
                break
        return index
        

    def binary_search(self, array, target):
        low, height = 0, len(array) - 1
        while low <= height:
            mid = low + (height - low) // 2
            if array[mid] > target:
                height = mid - 1
            elif array[mid] < target:
                low = mid + 1
            else:
                return True
        return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
