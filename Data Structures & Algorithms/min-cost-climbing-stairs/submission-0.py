class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one = cost[1]
        two = cost[0]

        for i in range(2,len(cost)):
            current = cost[i] + min(one,two)
            two = one
            one = current
        return min(one,two)