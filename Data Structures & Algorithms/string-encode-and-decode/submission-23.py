class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for str in strs:
            encoded += str+"[split]"
        return encoded

    def decode(self, s: str) -> List[str]:
      
        return s.split("[split]")[:-1]
