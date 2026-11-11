class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        res = []

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr_course = queue.popleft()
            res.append(curr_course)

            for nei in adj[curr_course]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)


        return res if len(res) == numCourses else []
