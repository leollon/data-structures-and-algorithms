"""Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
            profit = 6-1 = 5.
            Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import doctest


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Examples:

            >>> s = Solution()
            >>> prices = [7, 1, 5, 3, 6, 4]
            >>> s.maxProfit(prices)
            5
        """
        if not prices: return 0
        index = 0
        buy = prices[index]
        sell = 1
        profit = 0
        while index != len(prices) - 1:
            if prices[sell] > buy and prices[sell] - buy > profit:
                profit = prices[sell] - buy
            sell += 1
            if sell == len(prices):
                index += 1
                sell = index + 1
                buy = prices[index]
        return profit


if __name__ == "__main__":
    doctest.testmod(verbose=True)
