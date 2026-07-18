class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        cycle = set()
        adList = {i:[] for i in range(n)}

        for edge in edges:
            adList[edge[0]].append(edge[1])
            adList[edge[1]].append(edge[0])
        
        def dfs(node,parent):
            if node in cycle:
                return False

            cycle.add(node)

            for children in adList[node]:
                if children!=parent:
                    if dfs(children,node) == False:
                        return False
            cycle.remove(node)  

            return True

        return dfs(0,-1)
                            

