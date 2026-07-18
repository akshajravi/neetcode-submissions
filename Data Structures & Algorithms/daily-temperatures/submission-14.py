class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stack_indice = stack.pop()
                res[stack_indice] = i - stack_indice
            stack.append((t,i))
        return res
