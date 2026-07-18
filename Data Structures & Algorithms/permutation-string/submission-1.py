class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        s2Count = {}
        if len(s1) > len(s2):
            return False # s1 cannot be longer than s2, we want to find a permutation of s1 IN s2 
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i],0) + 1

        l = 0
        for r in range(len(s2)):
            s2Count[s2[r]] = s2Count.get(s2[r],0) + 1
            while (r - l + 1) > len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1
            if s2Count == s1Count:
                return True

        return False

