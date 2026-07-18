class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+','-','*','/']

        for token in tokens:
            if token in operands:
                int2 = int(stack.pop())
                int1 = int(stack.pop())
                res = 0
                if token == '+':
                    res = int1 + int2
                elif token == '-':
                    res = int1 - int2
                elif token == '*':
                    res = int1 * int2
                elif token == '/':
                    res = int(int1/int2)
                stack.append(str(res))
            else:
                stack.append(token)
        return int(stack[0])             

