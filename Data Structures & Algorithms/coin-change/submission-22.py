class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')
            
            if remaining in memo:
                return memo[remaining]

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + dp(remaining - coin))
            
            memo[remaining] = best

            return memo[remaining]

        result = dp(amount)

        return result if result != float('inf') else -1