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
        # brainstorm 1
        # Time Limit Exceeded
        # beg = 0
        # profit = 0
        # if len(prices) <= 1:
        #     return profit
        # profit = self._helper(prices[beg + 1:])
        # for i in range(len(prices) - 1):
        #     if prices[0] < prices[i + 1]:
        #         profit = max(profit, prices[i + 1] - prices[0])
        # return profit

        # brainstorm 2
        # failure edge case: [3, 4, 3]
        #  i = 0
        #  profit = 0
        #  while i < len(prices):
        #      new_prices = prices[i:]
        #      max_prices = max(new_prices)
        #      min_prices = min(new_prices)
        #      if new_prices.index(max_prices) > new_prices.index(min_prices):
        #          profit = max(profit, max_prices - min_prices)
        #      i += 1
        #  return profit
        if not prices:
            return 0
        buy_in_price = prices[0]  # buy a share of stock
        profit = i = 0
        while i < len(prices) - 1:
            # compare prices
            if prices[i + 1] > buy_in_price:
                # if current price is higher than buying, then sell a share of
                # stock
                profit = max(profit, prices[i + 1] - buy_in_price)
            else:
                # If you were only permitted to complete at most one
                # transaction (i.e., buy one and sell one share of the stock).
                # so if current price is lower than buy-in price, then buy a
                # share of stock.
                buy_in_price = prices[i + 1]
            i += 1
        return profit


if __name__ == "__main__":
    doctest.testmod(verbose=True)
