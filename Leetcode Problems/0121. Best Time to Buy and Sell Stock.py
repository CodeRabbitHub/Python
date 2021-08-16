# You are given an array prices where prices[i] is the price of a given stock
# on the ith day. You want to maximize your profit by choosing a single day to
# buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buy = 0
        sell = buy + 1
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return maxProfit


prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

s = Solution()

print(s.maxProfit(prices1))
print(s.maxProfit(prices2))
