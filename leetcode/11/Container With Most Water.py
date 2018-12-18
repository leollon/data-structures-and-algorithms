#!/usr/bin/python3
"""Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

一个容器能装多少容量的水取决与最短的那的那个木板。
"""


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
        while x0 != xn_1:
            capacity = min(height[x0], height[xn_1]) * (xn_1 - x0)
            max_capacity = max(capacity, max_capacity)
            if height[x0] < height[xn_1]:
                x0 += 1
            else:
                xn_1 -= 1
        return max_capacity


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
