class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numCities = len(isConnected)
        visited = [False] * numCities

        def dfs(city):
            visited[city] = True
            for nei in range(numCities):
                if isConnected[city][nei] and not visited[nei]:
                    dfs(nei)
        res = 0
        for i in range(numCities):
            if not visited[i]:
                dfs(i)
                res += 1

        return res