"""
Given an array A of non-negative integers, return an array consisting of all
the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.


Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
import doctest


class Solution:
    def sortArrayByParity(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        Examples:
            >>> s = Solution()
            >>> arr = [3, 1, 2, 4]
            >>> s.sortArrayByParity(arr)
            [4, 2, 3, 1]
            >>> arr = [3]
            >>> s.sortArrayByParity(arr)
            [3]
            >>> arr = [4, 3, 2, 5, 9, 10]
            >>> s.sortArrayByParity(arr)
            [10, 2, 4, 3, 5, 9]
            >>> arr = []
            >>> s.sortArrayByParity(arr)
            []
            >>> arr = [3, 4]
            >>> s.sortArrayByParity(arr)
            [4, 3]
            >>> arr = [3, 2, 4, 1]
            >>> s.sortArrayByParity(arr)
            [4, 2, 3, 1]
            >>> arr = [2, 4, 6, 8]
            >>> s.sortArrayByParity(arr)
            [8, 6, 4, 2]
        """
        length = len(arr)
        index = 0
        if not arr: return arr
        while index != length:
            if arr[index] % 2 == 0:
                even = arr.pop(index)
                arr.insert(0, even)
            index += 1
        return arr


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    s = Solution()