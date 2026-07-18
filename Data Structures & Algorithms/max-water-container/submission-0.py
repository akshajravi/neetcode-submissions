class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        max_level = 0

        while l < r:
            if heights[l] < heights[r]:
                level = heights[l] * (r-l)
                l +=1
            else:
                level = heights[r] * (r-l)
                r-=1
            if level > max_level:
                max_level = level
        return max_level
            
                
        