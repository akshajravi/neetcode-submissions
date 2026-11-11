class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        color = {}

        def dfs(node,c):
            color[node] = c
            for nei in graph[node]:
                if nei not in color:
                    if not dfs(nei, 1 - c):
                        return False
                elif color[nei] == c:
                    return False

            return True

        for i in range(len(graph)):
            if i not in color:
                if not dfs(i, 0):
                    return False

        return True