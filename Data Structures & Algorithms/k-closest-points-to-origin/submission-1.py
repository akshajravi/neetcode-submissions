class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]

            dist = -((x**2) + (y**2))**(.5)

            heapq.heappush(heap,[dist,x,y])

            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            dist,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res

