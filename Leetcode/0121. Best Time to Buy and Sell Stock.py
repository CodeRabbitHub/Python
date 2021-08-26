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
