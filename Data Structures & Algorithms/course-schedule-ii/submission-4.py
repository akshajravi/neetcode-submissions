class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        res = []

        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1


        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            res.append(course)
            for nei in adj[course]:
                indegree[nei] -=1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []

        





                



