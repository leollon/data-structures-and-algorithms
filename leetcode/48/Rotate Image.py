"""Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
import doctest


class Solution:
    def rotate(self, matrix) -> None:
        """Do not return anything, modify matrix in-place instead.
        :type matrix: List[List]
        :rtype: None

        Examples

            >>> s = Solution()
            >>> matrix = [
            ...     [1, 2, 3],
            ...     [4, 5, 6],
            ...     [7, 8, 9]
            ...  ]
            >>> s.rotate(matrix)
            >>> print(matrix)
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

            >>> matrix = [
            ...     [ 5, 1, 9,11],
            ...     [ 2, 4, 8,10],
            ...     [13, 3, 6, 7],
            ...     [15,14,12,16]
            ... ]
            >>> s.rotate(matrix)
            >>> print(matrix)
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

            >>> matrix = [[1]]
            >>> s.rotate(matrix)
            >>> print(matrix)
            [[1]]
        """
        size = len(matrix) - 1
        beg_row = beg_col = 0
        r = c = 0
        while beg_row <= size and beg_col <= size:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            c += 1
            if c == size + 1:
                beg_row += 1
                beg_col += 1
                r, c = beg_row, beg_col
        beg_col, end_col = 0, size
        r = 0
        while beg_col < end_col:
            matrix[r][beg_col], matrix[r][end_col] = matrix[r][end_col], matrix[r][beg_col]
            r += 1
            if r == size + 1:
                beg_col += 1
                end_col -= 1
                r = 0


if __name__ == "__main__":
    doctest.testmod(verbose=True)
