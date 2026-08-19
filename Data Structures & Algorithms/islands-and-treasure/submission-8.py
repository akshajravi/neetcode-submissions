class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        INF = 2147483647

        def addCell(r,c, dist):
            if (min(r,c) < 0 or r == ROWS or c == COLS  or grid[r][c] != INF):
                return

            grid[r][c] = dist
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])

        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                addCell(r + 1, c,dist)
                addCell(r-1,c, dist)
                addCell(r, c+1, dist)
                addCell(r, c-1, dist)



        
                    





        
