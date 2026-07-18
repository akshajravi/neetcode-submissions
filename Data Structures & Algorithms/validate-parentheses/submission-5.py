class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {']':'[','}':'{',')':'('}

        for i in range(len(s)):
            if s[i] not in keys:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != keys[s[i]]:
                    return False

        return len(stack) == 0