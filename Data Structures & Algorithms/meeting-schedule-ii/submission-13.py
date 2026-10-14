"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda interval : interval.start)
        if len(intervals) == 0:
            return 0
        heap = [intervals[0].end]

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if heap[0] <= start: #earliest ending meeting doesnt coincide with new meeting
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)
                

