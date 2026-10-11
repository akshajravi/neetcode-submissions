class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[0])
        count = 0
        last_interval = intervals[0]

        for i in range(1, len(intervals)):
            lastStart, lastEnd = last_interval
            start, end  = intervals[i]

            if start < lastEnd:
                last_interval = lastStart, min(end, lastEnd)
                count += 1

            else:
                last_interval = start,end

        return count

            
            
