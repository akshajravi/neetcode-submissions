class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        queue = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        finish = 0
        while queue:
            node = queue.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return finish == numCourses
            


