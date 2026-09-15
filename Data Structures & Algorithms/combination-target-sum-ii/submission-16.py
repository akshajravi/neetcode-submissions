class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # 1 2 2 4 5 6 9
        # 1 2 4 5 6 9
        res = []
        current = []

        def dfs(i, total):
            if total == target:
                res.append(current.copy())
                return 

            if total > target or i >= len(candidates):
                return 

            current.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            current.pop()

            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1,total)
        dfs(0,0)
        return res
            
                


                


