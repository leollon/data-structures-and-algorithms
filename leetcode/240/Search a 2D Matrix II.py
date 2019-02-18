"""Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

    1. Integers in each row are sorted in ascending from left to right.
    2. Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""
import doctest


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Examples

            >>> s = Solution()
            >>> matrix, target = [
            ...     [1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
            ...     [10,13,14,17,24],[18,21,23,26,30]
            ... ], 5
            >>> s.searchMatrix(matrix, target)
            True

            >>> matrix, target = [
            ...     [1,4,7,11],[2,5,8,12],[3,6,9,16],
            ...     [10,13,14,17], [18,21,23,26]
            ... ], 5
            >>> s.searchMatrix(matrix, target)
            True

            >>> matrix, target = [[1, 1]], 2
            >>> s.searchMatrix(matrix, target)
            False

            >>> matrix, target = [[5], [6]], 6
            >>> s.searchMatrix(matrix, target)
            True

            >>> matrix, target = [], 10
            >>> s.searchMatrix(matrix, target)
            False
        """
        if not matrix: return False
        col = len(matrix[0]) - 1
        row = 0
        while col >= 0 and row < len(matrix):
            right_top_most = matrix[row][col]
            if target > right_top_most:
                row += 1
            elif target < right_top_most:
                col -= 1
            else:
                return True
        return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
