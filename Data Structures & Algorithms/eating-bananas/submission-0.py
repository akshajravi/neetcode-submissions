class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_speed = max(piles)

        extra_hours = h - len(piles)
        min_speed = 1

        while min_speed < max_speed:
            k = (min_speed + max_speed) // 2
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            if time <= h:
                # going too fast, want to find the min time it takes that we can finish within given time
                max_speed = k 
            else:
                #going too slow
                min_speed = k + 1

        return min_speed
            
