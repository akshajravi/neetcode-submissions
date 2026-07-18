class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else: # if its not in pairs, it must be an opening brace
                stack.append(c)
        if not stack:
            return True
        else:
            return False
        