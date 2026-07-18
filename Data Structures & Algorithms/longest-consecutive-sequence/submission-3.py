class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_len = 0
        for num in nums:
            if num-1 not in nums:
                length = 1
                while num + length in nums:
                    length +=1
                max_len = max(length,max_len)

        return max_len
