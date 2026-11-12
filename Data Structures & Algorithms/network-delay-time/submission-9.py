class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0,k)]
        graph = {}

        for u,v,time in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, time))


        
        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue
            
            for nei, weight in graph.get(node, []):
                new_dist = d + weight 
                if new_dist < dist[nei]:
                    dist[nei] = new_dist

                    heapq.heappush(heap,(new_dist,nei))
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1
