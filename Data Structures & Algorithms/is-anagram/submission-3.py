class Solution:
    def getAlphabetIndex(self,alphabet:str):
        return ord(alphabet)-96

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr = [0 for i in range(26)]
        for i in range(len(s)):
            char_ab_index = self.getAlphabetIndex(s[i])
            arr[char_ab_index-1] +=1
            char_ab_index = self.getAlphabetIndex(t[i])
            arr[char_ab_index-1] -=1

        for val in arr:
            if val !=0:
                return False
        else:
            return True



        