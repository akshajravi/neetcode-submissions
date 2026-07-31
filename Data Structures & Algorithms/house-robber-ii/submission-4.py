class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        #case 1
        prev = nums[1]
        curr = max(nums[1],nums[2])
        for i in range(3,n):
            prev,curr = curr, max(nums[i] + prev, curr)
        option1 = curr

        #case2
        prev = nums[0]
        curr = max(nums[0],nums[1])
        for i in range(2,n-1):
            prev,curr = curr, max(nums[i] + prev, curr)
        option2 = curr

        return max(option1,option2)




        

            
