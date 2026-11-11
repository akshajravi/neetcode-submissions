class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]


        def dfs(r,c,visited,prev_height):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or visited[r][c] == True:
                return

            if prev_height > heights[r][c] :
                return

            visited[r][c] = True

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        #pacific
        for r in range(ROWS):
            dfs(r,0,pacific,0)
        for c in range(COLS):
            dfs(0,c,pacific,0)

        #atlantic
        for r in range(ROWS):
            dfs(r,COLS-1,atlantic,0)
        for c in range(COLS):
            dfs(ROWS-1,c, atlantic,0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if atlantic[r][c] and pacific[r][c]:
                    res.append([r,c])

        return res

                
                


            