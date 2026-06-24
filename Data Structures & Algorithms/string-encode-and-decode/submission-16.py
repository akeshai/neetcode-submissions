class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        chars = []
        for str_ in strs:
            lengths.append(str(len(str_)))
            chars.extend(list(str_))
        
        encodings = ",".join(lengths)+"[#]"+ "".join(chars)
        print("Encodings: ",encodings)
        return encodings

    def decode(self, s: str) -> List[str]:
        lengths,wstrings = s.split("[#]")
        strings = []
        lengths = eval(f"[{lengths}]"  ) 

        end  = 0
        start = 0
        for length in lengths:
            end = start + length
            str = wstrings[start:end]  

            strings.append(str)

            start  = end
        return strings
