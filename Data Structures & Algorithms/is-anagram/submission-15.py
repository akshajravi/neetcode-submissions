class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = [0] * 26
        b = [0] * 26
        for c in range(len(s)):
            a[ord(s[c]) - ord('a')] += 1
            b[ord(t[c]) - ord('a')] += 1

        return a == b
        

        


        