class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+','-','*','/']
        for c in tokens:
            if c in operands:
                b = stack.pop()
                a = stack.pop()

                a = int(a)
                b = int(b)


                result = 0

                if c == '+':
                    result = a + b
                elif c == '-':
                    result = a - b
                elif c == '*':
                    result = a * b
                elif c == '/':
                    result = int(a/b)
                stack.append(result)
            else:
                stack.append(int(c))
        return stack[0]


        