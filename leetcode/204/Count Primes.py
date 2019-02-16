"""Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import doctest


class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        primes = []
        for num in range(2, n):
            if self.is_prime(num):
                primes.append(num)
        return len(primes)
    
    def is_prime(self, n):
        i = 2
        while i <= int(math.sqrt(n)):
            if (n % i) == 0:
                return False
            i += 1
        return True



