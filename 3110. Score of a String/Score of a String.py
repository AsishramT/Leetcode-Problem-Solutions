class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_lst=[ord(char) for char in s]
        final_score=0
        for i in range(len(s)):
            if i+1<len(s):
                final_score+=abs(ascii_lst[i]-ascii_lst[i+1])
        return final_score
        
            




        