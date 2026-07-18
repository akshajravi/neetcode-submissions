class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
            for num in nums:
                if num not in used:
                    curr.append(num)
                    used.add(num)
                    dfs()
                    curr.pop()
                    used.remove(num)
        dfs()
        return res
                
