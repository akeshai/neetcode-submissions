class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(str_)) for str_ in strs]
        print(sorted_strs)
        groups = {}
        for i,str_ in enumerate(sorted_strs):
            if not str_ in groups:
                groups[str_] = [strs[i]]
            else:
                groups[str_].append(strs[i])
        print(groups)
        return list(groups.values())