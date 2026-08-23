class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        mapping = set(nums)
        return True if length != len(mapping) else False