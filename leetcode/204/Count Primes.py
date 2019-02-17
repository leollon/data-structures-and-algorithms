"""Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import doctest


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        
        Examples

            >>> s = Solution()
            >>> n = 10
            >>> s.countPrimes(n)
            4

            >>> n = 1
            >>> s.countPrimes(n)
            0

            >>> n = 499979
            >>> s.countPrimes(n)
            41537
        """
        if n <= 1: return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return primes.count(True)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
