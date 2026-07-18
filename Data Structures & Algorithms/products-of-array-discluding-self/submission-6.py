class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = [1] * len(nums)
        multiplier = 1
        for i in range(len(nums)):
            array[i] *= multiplier
            multiplier *= nums[i]

        multiplier = 1

        for j in range(len(nums)-1,-1,-1):
            array[j] *= multiplier
            multiplier *= nums[j]
        return array