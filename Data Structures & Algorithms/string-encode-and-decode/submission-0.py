import random
class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_string = str(strs)     
        encoded_str = ""
        for i,char in enumerate(combined_string):
            encoded_str+=str(ord(char))
            if not i == len(combined_string)-1:
                encoded_str+="[sep]"
        return encoded_str


    def decode(self, s: str) -> List[str]:
        combined_string = ''
        for char in s.split("[sep]"):
            combined_string+=chr(int(char))
        

        return eval(combined_string)
            

