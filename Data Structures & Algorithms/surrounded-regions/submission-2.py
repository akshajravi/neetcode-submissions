class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        safe = [[False] * cols for _ in range(rows)]
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols):
                return
            if board[r][c] == 'X':
                return
            if safe[r][c] == True:
                return

            safe[r][c] = True

            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)

        for r in range(rows):
            for c in range(cols):
                if not safe[r][c]:
                    board[r][c] = 'X'
            
