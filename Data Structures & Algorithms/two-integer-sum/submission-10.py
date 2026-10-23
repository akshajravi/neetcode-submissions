class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            want = target - nums[i]
            if want in pairs:
                return [pairs[want],i]
            pairs[nums[i]] = i
        