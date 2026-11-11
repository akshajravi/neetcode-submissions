class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #1. create adj list
        #pairs are built as [course, prereq]

        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0

        while queue:
            curr_course = queue.popleft()
            count += 1

            for nei in adj[curr_course]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)

        return numCourses == count




