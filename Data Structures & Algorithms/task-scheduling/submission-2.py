class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0
        queue = deque()
        #creates a dict that has value:count pairs
        count = Counter(tasks)
        #use max heap since higher count gets higher priority
        heap = [-x for x in count.values()] 
        heapq.heapify(heap)

        while heap or queue:
            time += 1

            if not heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append([cnt,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap,queue.popleft()[0])

        return time