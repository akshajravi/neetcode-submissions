class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visiting = set()
        visited = set()
        adj = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        
