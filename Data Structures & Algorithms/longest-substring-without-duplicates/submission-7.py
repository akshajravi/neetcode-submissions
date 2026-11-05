class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        longest = 0

        l = 0

        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            tracker.add(s[r])
            longest = max(longest, r - l + 1)

        return longest


                

