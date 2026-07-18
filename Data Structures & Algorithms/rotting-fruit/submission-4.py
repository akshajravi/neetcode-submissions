class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        q = deque()


        def bfs(r,c):
            if(r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 2 or grid[r][c] == 0):
                return
            grid[r][c] = 2
            q.append((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

        minutes = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            if q:
                minutes += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return minutes




