class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                profit = prices[i] - prices[buy]
                max_profit = max(profit, max_profit)
        return max_profit