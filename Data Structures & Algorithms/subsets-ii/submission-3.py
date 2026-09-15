class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def bt(i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            bt(i + 1)
            curr.pop()


            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            bt(i + 1)

        bt(0)
        return res
            
            