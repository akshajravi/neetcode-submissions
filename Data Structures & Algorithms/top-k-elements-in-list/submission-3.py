class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        heap = []
        for value, freq in count.items():
            heapq.heappush(heap,(freq,value))
            if len(heap) > k:
                heapq.heappop(heap)
        for num in heap:
            freq, value = num
            res.append(value)
        return res
