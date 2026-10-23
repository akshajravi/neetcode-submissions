class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set(nums)

        return len(checker) != len(nums)