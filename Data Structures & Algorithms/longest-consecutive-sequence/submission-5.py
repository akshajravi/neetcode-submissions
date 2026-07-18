class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count , maxCount = 1,0 
        numSet = set(nums)
        for num in numSet:
            count = 1
            if num - 1 not in numSet:
                while num + 1 in numSet:
                    count += 1
                    num += 1
                maxCount = max(maxCount,count)
        return maxCount
