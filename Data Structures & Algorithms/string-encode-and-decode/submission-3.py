class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for str in strs:
            parts.append(f"{len(str)}#{str}")
        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        delim = '#'
        temp = []
        result = []
        i = 0
        while i < len(s):
            if s[i] == delim:
                length = int("".join(temp))
                temp = []
                result.append(s[i+1: i + length + 1])
                i += length + 1
            else:
                temp.append(s[i])
                i += 1
        return result