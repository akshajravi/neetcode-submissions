class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        heap = []

        for key, value in frequency.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        while heap:
            count, element = heapq.heappop(heap)
            res.append(element)
        return res