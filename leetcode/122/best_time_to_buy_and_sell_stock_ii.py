"""
Say you have an array prices for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock
multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

Example 1:

    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5),
    profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5
    (price = 6), profit = 6-3 = 3.

Example 2:

    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
    profit = 5-1 = 4. Note that you cannot buy on day 1, buy on day 2 and
    sell them later, as you are engaging multiple transactions at the same
    time. You must sell before buying again.

Example 3:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

    - 1 <= prices.length <= 3 * 10 ^ 4
    - 0 <= prices[i] <= 10 ^ 4
"""
import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_in_price = prices[0]
        profit = i = 0
        while i < len(prices) - 1:
            # You may complete as many transactions as you like (i.e., buy one
            # and sell one share of the stock multiple times).

            i += 1
            if prices[i] > buy_in_price:
                # sell a share of stock after peak from the valley
                profit += prices[i] - buy_in_price
            # buy in again when in valley
            buy_in_price = prices[i]
        return profit


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProfit(self):

        prices = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(6, self.solution.maxProfit(prices))

        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(7, self.solution.maxProfit(prices))

        prices = [3, 4, 2, 1]
        self.assertEqual(1, self.solution.maxProfit(prices))

        prices = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(0, self.solution.maxProfit(prices))


if __name__ == "__main__":
    unittest.main()

