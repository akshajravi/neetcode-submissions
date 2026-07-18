class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        components = 0
        visited = set()

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                components +=1
                dfs(node)
        return components
             
