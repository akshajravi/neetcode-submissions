class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        res = float('-inf')
        curSum = 0

        while i < len(nums):
            if curSum < 0:
                curSum = 0
            
            curSum += nums[i]
            res = max(curSum, res)

            i+= 1


        return res
