class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(len(prices)):
            sell = prices[i]
            if i > 0:
                buy = min(prices[0:i])
            else:
                buy = prices[i]
            profit = sell - buy
            if profit < 0:
                profit = 0
            if profit > max_profit:
                max_profit = profit
        return max_profit
            

        