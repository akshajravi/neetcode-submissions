class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        res = []
        visit = set()
        cycle = set()

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for courses in preMap[crs]:
                if dfs(courses) == False:
                    return False
            visit.add(crs)
            cycle.remove(crs)
            res.append(crs)

            
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res 

