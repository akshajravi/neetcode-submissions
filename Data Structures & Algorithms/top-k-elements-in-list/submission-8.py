class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for key, value in freq.items():
            buckets[value].append(key)

        res = []
        count = 0
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res



        
