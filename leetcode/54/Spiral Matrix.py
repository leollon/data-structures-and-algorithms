#!/usr/bin/python3
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:

    Input:
    [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Examples:

            >>> s = Solution()
            >>> matrix = [
            ...     [ 1, 2, 3 ],
            ...     [ 4, 5, 6 ],
            ...     [ 7, 8, 9 ]
            ... ]
            >>> s.spiralOrder(matrix)
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
            >>> matrix = [
            ...     [1, 2, 3],
            ...     [4, 5, 6]
            ... ]
            >>> s.spiralOrder(matrix)
            [1, 2, 3, 6, 5, 4]
            >>> matrix = [
            ...     [1, 2, 3],
            ...     [4, 5, 6],
            ...     [7, 8, 9],
            ...     [10, 11, 12],
            ...     [13, 14, 15]
            ... ]
            >>> s.spiralOrder(matrix)
            [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]
            >>> matrix = [
            ...     [1, 2],
            ...     [3, 4],
            ...     [5, 6]
            ... ]
            >>> s.spiralOrder(matrix)
            [1, 2, 4, 6, 5, 3]
        """
        if not len(matrix): return []
        row_beg, col_beg, row_end, col_end = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        result = []
        while True:
            # From left to right
            col = col_beg
            while col <= col_end:
                result.append(matrix[row_beg][col])
                col += 1
            row_beg += 1
            if row_beg > row_end: break  # 只剩下一行或者是只有单行
            # From top to bottom
            row = row_beg
            while row <= row_end:
                result.append(matrix[row][col_end])
                row += 1
            col_end -= 1
            if col_beg > col_end: break  # 只剩下一列或者是只有单列
            # From right to left
            col = col_end
            while col >= col_beg:
                result.append(matrix[row_end][col])
                col -= 1
            row_end -= 1
            if row_beg > row_end: break  # 最后一行
            # From bottom to top
            row = row_end
            while row >= row_beg:
                result.append(matrix[row][col_beg])
                row -= 1
            col_beg += 1
            if col_beg > col_end: break  # 最后一列
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
