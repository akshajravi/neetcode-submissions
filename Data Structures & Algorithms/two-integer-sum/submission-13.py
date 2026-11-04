class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums[i] + nums[j] = target
        # target - nums[j] = nums[i]

        hashmap = {}

        for idx, num in enumerate(nums):
            ans = target - num
            if ans in hashmap:
                return [hashmap[ans], idx]
            hashmap[num] = idx