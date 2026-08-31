from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        1. For each point calculate distance to origin
        2. Push all to min heap
        3. Pop from min heap until len = k
        4. return the rest
        '''

        heap = []
        for point in points:
            x,y = point[0], point[1]
            dist = sqrt((x)**2 + (y)**2)
            heapq.heappush(heap, (-dist, [x,y]))

        while len(heap) > k:
            heapq.heappop(heap)

        res = []

        while len(heap) > 0:
            dist,array  = heapq.heappop(heap) 
            dist = -dist

            res.append(array)
        return res


            

        