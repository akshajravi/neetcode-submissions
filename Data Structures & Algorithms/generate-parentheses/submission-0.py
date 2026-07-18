class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        stack = []
        result = []

        def backtrack(openN, closedN):

            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() #bc the stack is sort of a global variable
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0,0)
        return result