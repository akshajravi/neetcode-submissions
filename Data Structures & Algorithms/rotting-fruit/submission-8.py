class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))

                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        while queue and fresh > 0:
            curr_level = len(queue)
            for _ in range(curr_level):
                r,c = queue.popleft()
                for x,y in directions:
                    if x + r >= 0 and x + r < ROWS and y + c >= 0 and y + c < COLS and grid[x + r][y + c] == 1:
                        queue.append((x + r, y + c))
                        grid[x + r][c + y] = 2
                        fresh -=1
            time += 1

        return time if fresh == 0 else -1





