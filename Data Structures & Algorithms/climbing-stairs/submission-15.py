class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1 way to get to the first stair, 2 ways to get to the second stair
        getting to any stair k where k > 2 is just the sum of ways to get to the previous 2 stairs
        '''

        if n <= 2:
            return n

        last_last = 1
        last = 2 

        for i in range(2,n):
            temp = last_last + last
            last,last_last = temp,last

        return last