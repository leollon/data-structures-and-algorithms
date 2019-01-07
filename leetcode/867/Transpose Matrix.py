#!/usr/bin/python3
"""Transpose Matrix
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]

        Examples

            >>> nums = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
            >>> Solution().transpose(nums)
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

            >>> nums = [[1, 2, 3],[4, 5, 6]]
            >>> Solution().transpose(nums)
            [[1, 4], [2, 5], [3, 6]]
            
            >>> nums = [[1, 2],[3, 4]]
            >>> Solution().transpose(nums)
            [[1, 3], [2, 4]]

        """
        new_array = []
        for i in range(len(A[0])):
            sub_array = []
            for j in range(len(A)):
                sub_array.append(A[j][i])
            new_array.append(sub_array[:])
            sub_array.clear()
        return new_array


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)