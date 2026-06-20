class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        hashs = {}
        hasht = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in hashs:
                hashs[char_s]+=1
            else:
                hashs[char_s] = 1
            
            if char_t in hasht:
                hasht[char_t]+=1
            else:
                hasht[char_t] = 1
            

        return hasht==hashs
                    

