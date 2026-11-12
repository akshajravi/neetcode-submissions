class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_back = 2
        two_back = 1

        for i in range(2,n):
            temp = one_back + two_back
            two_back = one_back
            one_back = temp 


        return one_back
