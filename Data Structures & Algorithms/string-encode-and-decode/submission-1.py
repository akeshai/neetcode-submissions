import random
class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_string = str(strs)     
        encoded_str = []
        for i,char in enumerate(combined_string):
            encoded_str.extend([str(ord(char)),'[sep]'])
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        combined_string = ''
        for char in s.split("[sep]")[:-1]:
            combined_string+=chr(int(char))
        return eval(combined_string)
            

