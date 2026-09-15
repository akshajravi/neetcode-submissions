class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two, one = cost[0],cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(one,two)

            two, one = one, current

        
        return min(one,two)

        

        
        