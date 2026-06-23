class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # step 1 create a empity hash
        groups = {}
        # loop strs and sort string and set as key and assign it an empity array in hash ,
        # if key already exist, append unsorted string in that key array.

        for str_ in strs:
            sorted_str_ = ''.join(sorted(str_))
            if not sorted_str_ in groups:
                groups[sorted_str_] = [str_]
                continue
            groups[sorted_str_].append(str_)

        return list(groups.values())