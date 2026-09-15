class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        res = []

        def dfs(open_num, closed_num):
            if open_num == closed_num == n:
                res.append("".join(curr))
                return

            if open_num < n:
                curr.append("(")
                dfs(open_num + 1, closed_num)
                curr.pop()

            if closed_num < open_num:
                curr.append(")")
                dfs(open_num, closed_num + 1)
                curr.pop()

            
        dfs(0,0)
        return res

            
            