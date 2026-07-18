class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #store difference in hashmap : key is difference and value is index
        for i in range(len(nums)):
            curr = nums[i]
            difference = target - curr
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[curr] = i