class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest_length = 0;
        for num in nums:
            if (num - 1) not in my_set:
                current_num = num
                current_len = 1
                while current_num + 1 in my_set:
                    current_len +=1
                    current_num +=1
                longest_length = max(current_len, longest_length)
        return longest_length

        