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
        array = list(range(1, n + 1))
        return self.remove(array, len(array))

    def remove(self, array, length):
        if length == 1:
            return array[0]
        else:
            new_array = list(reversed(array[1:length:2]))
            length = len(new_array)
            return self.remove(new_array, length)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
