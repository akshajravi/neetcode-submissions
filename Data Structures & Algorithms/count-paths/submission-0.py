class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        for i in range(n):
            cache[m-1][i] = 1

        for j in range(m):
            cache[j][n-1] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2,-1,-1):
                cache[i][j] = cache[i + 1][j] + cache[i][j+1]
        return cache[0][0]