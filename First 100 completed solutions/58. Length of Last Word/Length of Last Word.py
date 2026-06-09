class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=s.split()[-1]
        return len(lst)

        