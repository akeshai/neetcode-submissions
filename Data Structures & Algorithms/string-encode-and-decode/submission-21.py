class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        lengths = []
        chars = []
        for str_ in strs:
            lengths.append(str(len(str_)))
            chars.extend(list(str_))
        encodings = ",".join(lengths)+"[#]"+ "".join(chars)
        return encodings

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        lengths,wstrings = s.split("[#]")
        strings = []
        lengths = lengths.split(',')
        # print("lengths: ",lengths)
        end  = 0
        start = 0
        for length in lengths:
            end = start + int(length)
            str = wstrings[start:end]  
            strings.append(str)
            start  = end
        return strings
