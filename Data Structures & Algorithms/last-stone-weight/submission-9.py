class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap) * -1
            stone2 = heapq.heappop(heap) * -1

            new_stone = (stone1 - stone2) * -1

            heapq.heappush(heap, new_stone)

        return -heap[0] if heap else 0
