"""
There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every
third bulb (turning on if it's off or turning off if it's on).
For the i-th round, you toggle every i bulb.
For the n-th round, you only toggle the last bulb.
Find how many bulbs are on after n rounds.

Example:

    Input: 3
    Output: 1
    Explanation:
    At first, the three bulbs are [off, off, off].
    After first round, the three bulbs are [on, on, on].
    After second round, the three bulbs are [on, off, on].
    After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
"""
import math


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int

        Examples

            >>> s = Solution()
            >>> n = 0
            >>> s.bulbSwitch(n)
            0

            >>> n = 1
            >>> s.bulbSwitch(n)
            1

            >>> n = 3
            >>> s.bulbSwitch(n)
            1

            >>> n = 4
            >>> s.bulbSwitch(n)
            2

            >>> n = 5
            >>> s.bulbSwitch(n)
            2

            >>> n = 10
            >>> s.bulbSwitch(n)
            3
        """
        bulbs = [1] * n
        if n <= 1:
            return bulbs.count(1)
        i = 2
        while i < n:
            start = i - 1
            while start < n:
                bulbs[start] = not bulbs[start]
                start += i
            i += 1
        bulbs[n - 1] = not bulbs[n - 1]
        return bulbs.count(1)


class BestSolution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int

        Examples

            >>> s = Solution()
            >>> n = 0
            >>> s.bulbSwitch(n)
            0

            >>> n = 1
            >>> s.bulbSwitch(n)
            1

            >>> n = 3
            >>> s.bulbSwitch(n)
            1

            >>> n = 4
            >>> s.bulbSwitch(n)
            2

            >>> n = 5
            >>> s.bulbSwitch(n)
            2

            >>> n = 10
            >>> s.bulbSwitch(n)
            3
        """
        return int(math.sqrt(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
