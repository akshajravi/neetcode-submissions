class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dp(j))

            memo[i] = best
            return best
        return max(dp(i) for i in range(n))
        

            