class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                #turn list in tuple since lists are mutable and can't be dictionary keys
            res[tuple(count)].append(s)
            
        return list(res.values())
