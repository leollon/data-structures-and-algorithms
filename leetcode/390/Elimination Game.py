"""Elimination Game

"""
import doctest


class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int

        Examples

            >>> s = Solution()
            >>> n = 1
            >>> s.lastRemaining(n)
            1

            >>> n = 9
            >>> s.lastRemaining(n)
            6

            >>> n = 8160
            >>> s.lastRemaining(n)
            4086

            >>> n = 100000000
            >>> s.lastRemaining(n)
            32896342
        """
        left = True
        first, step = 1, 1
        while n > 1:
            if left or n % 2 == 1:
                first += step
            n >>= 1
            step <<= 1
            left = not left
        return first


if __name__ == "__main__":
    doctest.testmod(verbose=True)
