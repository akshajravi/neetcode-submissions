class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        #2 cases : rob first house and dont rob last, or rob from 2nd and rob last

        #robbing first house
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            prev, curr = curr, max(prev + nums[i], curr)

        rob1 = curr

        #rob from 2nd + last

        prev = nums[1]
        curr = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)

        rob2 = curr

        return max(rob1,rob2)


        