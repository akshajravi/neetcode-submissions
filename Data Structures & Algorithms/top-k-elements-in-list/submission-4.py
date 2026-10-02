class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []

        # we want to push (value,key) into heap
        #python is min heap by default, so we have to negate values before pushing  
        for num, freq in count.items():
            heapq.heappush(heap,(freq,num))
            while len(heap) > k:
                heapq.heappop(heap)



        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

        