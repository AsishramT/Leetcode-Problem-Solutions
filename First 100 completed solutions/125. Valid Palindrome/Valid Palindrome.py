from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.translate(str.maketrans("", "", punctuation)).lower().replace(" ","")
        if not s:
            return True
        return s==s[::-1]
