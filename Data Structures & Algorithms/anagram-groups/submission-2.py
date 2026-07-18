class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_string = sorted(s)
            res[tuple(sorted_string)].append(s)
        return list(res.values())