#!/usr/bin/env python3
"""Given a positive integer n, generate a square matrix filled
with elements from 1 to pow(n, 2) in spiral order.

Example:
    Input: 3
    Output:
    [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
    ]
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Examples:

            >>> s = Solution()
            >>> n = 1
            >>> s.generateMatrix(n)
            [[1]]
            >>> n = 2
            >>> s.generateMatrix(n)
            [[1, 2], [4, 3]]
            >>> n = 3
            >>> s.generateMatrix(n)
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        """
        if n <= 0: return None
        result = [[0] * n for _ in range(n)]
        # ret_val = [[0] * n] * n # 错误的方法，数组的每行都是引用同一个包含n个元素的列表对象
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, (n*n) + 1):
            result[i][j] = k
            if result[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
