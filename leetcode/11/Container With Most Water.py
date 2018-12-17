#!/usr/bin/python3
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Examples:
            >>> s = Solution()
            >>> height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
            >>> s.maxArea(height)
            49
            >>> height = [8, 1, 6, 2, 5, 4, 8, 3, 7]
            >>> s.maxArea(height)
            56
            >>> height = [8, 1]
            >>> s.maxArea(height)
            1
            >>> height = [1, 2]
            >>> s.maxArea(height)
            1
            >>> height = [1, 9, 2, 1, 3, 4, 9]
            >>> s.maxArea(height)
            45
        """
        max_capacity = 0
        x0, xn_1 = 0, len(height) - 1
        while True:
            if x0 == len(height) - 1: break
            min_val = min(height[x0], height[xn_1])
            capacity = min_val * (xn_1 - x0)
            if capacity > max_capacity:
                max_capacity = capacity
            xn_1 -= 1
            if xn_1 == x0:
                x0 += 1
                xn_1 = len(height) - 1
        return max_capacity


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
