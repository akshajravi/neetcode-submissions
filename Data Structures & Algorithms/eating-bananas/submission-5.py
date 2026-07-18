class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        l,r = 1, max(piles)
        min_hours = float('inf')
        while l <= r:
            mid = (l+r) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                min_hours = min(hours, min_hours)
                r = mid - 1
            else:
                l = mid + 1
            
        return l

