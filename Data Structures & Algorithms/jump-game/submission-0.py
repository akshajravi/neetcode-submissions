class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:#its possible to reach the next spot we need to be at
                goal = i
        return goal == 0 


        
