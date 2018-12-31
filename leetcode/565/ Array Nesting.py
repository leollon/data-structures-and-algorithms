#!/usr/bin/python3
"""Array Nesting
A zero-indexed array A of length N contains all integers from 0 to N-1.
Find and return the longest length of set S, where
S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of
element A[i] of index = i, the next element in S should be A[A[i]],
and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate
element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
 

Note:

    1.N is an integer within the range [1, 20,000].
    2.The elements of A are all distinct.
    3.Each element of A is an integer within the range [0, N-1].
"""


class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Examples:

            >>> s = Solution()
            >>> nums = [5, 4, 0, 3, 1, 6, 2]
            >>> s.arrayNesting(nums)
            4
            >>> nums = [8, 0, 1, 3, 2, 4, 5, 7, 1]
            >>> s.arrayNesting(nums)
            3
            >>> nums = [0, 2, 1]
            >>> s.arrayNesting(nums)
            2
        """
        if not nums: return 0
        visited_index = set()
        max_length, count, index = 1, 1, 0
        start = nums[index]
        next_ele = nums[start]
        while True:
            visited_index.add(start)
            if next_ele != start and next_ele not in visited_index:
                visited_index.add(next_ele)
                next_ele = nums[next_ele]
                count += 1
                continue
            max_length = max(count, max_length)
            count = 1
            index += 1
            if index in visited_index:
                index += 1
            if index >= len(nums): break
            start = nums[index]
            next_ele = nums[start]
        return max_length


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
