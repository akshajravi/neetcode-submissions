class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i,remaining):

            if remaining == 0:
                return 1
            if i == len(coins) or remaining < 0:
                return 0

            if (i,remaining) in cache:
                return cache[(i,remaining)]

            # we can either take the coin or skip it 
            
            take = dfs(i, remaining - coins[i])
            skip = dfs(i + 1, remaining)

            cache[(i,remaining)] = take+skip

            return cache[(i,remaining)]
        return dfs(0, amount)
