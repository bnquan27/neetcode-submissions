class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        clean_text = "".join(char for char in s if char.isalpha() or char.isdigit())
        i = 0
        j = len(clean_text) - 1
        while (i < j):
            if clean_text[i] != clean_text[j]:
                return False
            i += 1
            j -= 1
        return True