class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)

        max_len = 0

        for num in nums:
            if num-1 not in my_set:
                curr_num = num
                length = 1
                while curr_num + length in my_set:
                    length +=1
                max_len = max(length,max_len)

        return max_len
        