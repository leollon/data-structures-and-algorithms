"""Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3

Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Exampls

            >>> s = Solution()
            >>> n = 1
            >>> s.climbStairs(n)
            1

            >>> n = 2
            >>> s.climbStairs(n)
            2

            >>> n = 5
            >>> s.climbStairs(n)
            8

            >>> n = 10
            >>> s.climbStairs(n)
            89

            >>> n = 20
            >>> s.climbStairs(n)
            10946

            >>> n = 6
            >>> s.climbStairs(n)
            13

            >>> n = 38
            >>> s.climbStairs(n)
            63245986
        """
        a, b = 1, 1
        while n - 1 > 0:
            a = a + b
            a, b = b, a
            n -= 1
        return b


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
