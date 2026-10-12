class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        current = []

        def bt(i,amount):

            if amount == target:
                res.append(current.copy())
                return

            if amount > target or i >= len(candidates):
                return

            current.append(candidates[i])
            bt(i + 1, amount + candidates[i])
            current.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bt(i + 1, amount)

        bt(0,0)
        return res
            
            
        
