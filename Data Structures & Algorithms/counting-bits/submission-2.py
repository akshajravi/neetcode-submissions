class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [] 
        for num in range(n + 1):
            num_res = 0
            for i in range(32):
                num_res += 1 if (1 << i) & num else 0
            res.append(num_res)
        return res
            