class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # step 1 create array vector for each string and
        # compair them with there vector representation
        group = {}
        for str_ in strs:
            array = [0]*26

            for char in str_:
                char_idx = ( ord(char)- ord('a') )
                array[char_idx]+=1
            if not tuple(array) in group:
                group[tuple(array)] = [str_]
                
            else:
                group[tuple(array)].append(str_)


        return list(group.values())


            


        
        
