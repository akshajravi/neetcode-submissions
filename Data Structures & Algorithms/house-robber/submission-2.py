class Solution:
    def rob(self, nums: List[int]) -> int:
        two_house_back, prev_house = 0,0 
        for num in nums:
            temp = max(two_house_back + num, prev_house)
            two_house_back = prev_house
            prev_house = temp
        return prev_house
