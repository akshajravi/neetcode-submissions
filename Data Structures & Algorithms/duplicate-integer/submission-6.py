class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        #if any value appears more than once, len(set) should be shorter than len(nums)

        return len(nums) != len(my_set)