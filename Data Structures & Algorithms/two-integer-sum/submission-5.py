class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in diffs:
                return [diffs[curr], i]
            diffs[nums[i]] = i