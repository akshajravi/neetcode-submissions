class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return 

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    break
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()

        backtrack(0,[],0)
        return res

