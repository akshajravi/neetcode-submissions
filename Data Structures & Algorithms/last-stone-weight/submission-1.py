class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-x for x in stones]

        heapq.heapify(heap)

        while len(heap) > 1: #fix this its probably not right
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)

            if y < x:
                heapq.heappush(heap,-1*(x-y))
        
        if heap:
            return heap[0] * -1
        return 0

