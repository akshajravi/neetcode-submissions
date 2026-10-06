class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows,cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False]* cols for _ in range(rows)]
        res = []

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c,visited,prev_height):
            if r<0 or c<0 or r >= rows or c>=cols:
                return

            if heights[r][c] < prev_height:
                return

            
            if visited[r][c] == True:
                return
            
            visited[r][c] = True

            for dr, dc in directions:
                dfs(dr + r, dc + c, visited, heights[r][c])

        
        #from atlantic
        for r in range(rows):
            dfs(r,cols-1,atlantic,0)
        for c in range(cols):
            dfs(rows-1,c,atlantic,0)
        
        #from pacific
        for r in range(rows):
            dfs(r,0,pacific,0)
        for c in range(cols):
            dfs(0,c,pacific,0)
        

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
        return res

