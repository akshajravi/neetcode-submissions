class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()

                for x,y in directions:
                    r_new, c_new = r + x, c + y
                    if r_new in range(rows) and c_new in range(cols) and grid[r_new][c_new] == 1:
                        grid[r_new][c_new] = 2
                        q.append((r_new,c_new))
                        fresh -=1
            time += 1
        

        return time if fresh == 0 else -1


                    
                        
