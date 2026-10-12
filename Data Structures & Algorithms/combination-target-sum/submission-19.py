class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []

        def bt(i,amount):
            if amount == target:
                res.append(path.copy())
                return

            if (i >= len(nums)) or amount > target:
                return

            
            path.append(nums[i])
            bt(i, amount + nums[i])
            path.pop()
            bt(i + 1, amount)

        bt(0,0)

        return res