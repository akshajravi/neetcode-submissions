class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = [[False]* cols for _ in range(rows)]
        
        def addCell(r,c):
            if(r < 0 or c < 0 or r >= rows or c >= cols or visit[r][c] or grid[r][c] == -1):
                return
            q.append((r,c))
            visit[r][c] = True


        #starts queue with locations of treasure
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit[r][c] = True
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        
        
        

