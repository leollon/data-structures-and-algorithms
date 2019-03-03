"""Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the two
preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

    0 ≤ N ≤ 30.
"""


class Solution:
    def fib(self, N: int) -> int:
        """

        Examples

            >>> s = Solution()
            >>> N = 0
            >>> s.fib(N)
            0

            >>> N = 1
            >>> s.fib(N)
            1
            
            >>> N = 2
            >>> s.fib(N)
            1
            
            >>> N = 25
            >>> s.fib(N)
            75025
            
            >>> N = 30
            >>> s.fib(N)
            832040
        """
        first, second = 0, 1
        result = 0
        if N == 1:
            result = 1
        while N >= 2:
            result = first + second
            first, second = second, result
            N -= 1
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
