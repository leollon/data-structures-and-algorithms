"""Counting Bits
Given a non negative integer number num. For every numbers i in the
range 0 ≤ i ≤ num calculate the number of 1's in their binary representation
and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

    1. It is very easy to come up with a solution with run time
    O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
    single pass?

    2. Space complexity should be O(n).

    3. Can you do it like a boss? Do it without using any builtin function
    like __builtin_popcount in c++ or in any other language.
"""


class Solution1:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]

        Examples
        
            >>> s = Solution1()
            >>> num = 2
            >>> s.countBits(num)
            [0, 1, 1]
            >>> num = 5
            >>> s.countBits(num)
            [0, 1, 1, 2, 1, 2]
        """
        result = []
        for i in range(num + 1):
            result.append(bin(i).count('1'))
        return result


class Solution2:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]

        Examples
        
            >>> s = Solution2()
            >>> num = 2
            >>> s.countBits(num)
            [0, 1, 1]
            >>> num = 5
            >>> s.countBits(num)
            [0, 1, 1, 2, 1, 2]
        """
        result = []
        count = 0
        for i in range(num + 1):
            while i:
                if (i % 2):
                    count += 1
                i //= 2
            result.append(count)
            count = 0
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
