class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str_ in (strs):
            sorted_str = ''.join(sorted(str_))
            if not sorted_str in groups:
                groups[sorted_str] = [str_]
                continue
            
            groups[sorted_str].append(str_)
        return list(groups.values())