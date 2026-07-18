class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        atlantic = [[False] * cols for _ in range(rows)]
        pacific = [[False] * cols for _ in range(rows)]
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        res = []

        def dfs(r, c, visited, prev_height):
            if(r < 0 or c < 0 or r >= rows or c >= cols):
                return
            if heights[r][c] < prev_height:
                return
            if visited[r][c]:
                return
            
            visited[r][c] = True

            for dr, dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])

        #call from pacific border
        for c in range(cols):
            dfs(0,c,pacific,0)
        for r in range(rows):
            dfs(r,0,pacific,0)
        
        #call from atlantic border
        for c in range(cols):
            dfs(rows-1,c,atlantic,0)
        for r in range(rows):
            dfs(r,cols-1,atlantic,0)

        for r in range(rows):
            for c in range(cols):
                if atlantic[r][c] and pacific[r][c]:
                    res.append([r,c])
        return res




