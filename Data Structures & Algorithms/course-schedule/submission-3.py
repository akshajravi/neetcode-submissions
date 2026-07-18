class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #maps each course to the required prereqs
        preMap = {i:[] for i in range(numCourses)}
        visited = set()

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(course):
            #already counted course as a prereq, we're in a cycle
            if course in visited:
                return False
            #prereqs are already compeleted/ no prereq           |
            if preMap[course] == []:
                return True
            
            visited.add(course)

            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


            