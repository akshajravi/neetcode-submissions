class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = dr+row
                    nc = dc + col
                    if (nc < 0 or nr < 0 or nc >= cols or nr >= rows or grid[nr][nc] == 0):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(bfs(r,c),max_area)
        return max_area
        