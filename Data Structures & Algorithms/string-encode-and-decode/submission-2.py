class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for str in strs:
            result += f"{len(str)}#{str}"
        return result
    def decode(self, s: str) -> List[str]:
        delim = '#'
        temp = ""
        result = []
        i = 0
        while i < len(s):
            if s[i] == delim:
                length = int(temp)
                temp = ""
                result.append(s[i+1: i + length + 1])
                i += length + 1
            else:
                temp+=s[i]
                i += 1
        return result