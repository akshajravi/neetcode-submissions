class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for a in asteroids:
            while stack and (a ^ stack[-1]) < 0:
                if a > 0:
                    stack.append(a)
                    break
                else:
                    if abs(stack[-1]) < abs(a):
                        stack.pop()
                    elif abs(stack[-1]) == abs(a):
                        stack.pop()
                        break
                    else:
                        break
            else: 
                stack.append(a)
        return stack


        