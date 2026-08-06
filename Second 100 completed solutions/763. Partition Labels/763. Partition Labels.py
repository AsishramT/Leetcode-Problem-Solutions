class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i, letter in enumerate(s):
            last[letter] = i

        ans = []

        start = 0
        end = 0
        
        for i in range(len(s)):
            end=max(end,last[s[i]])

            if i == end:
                ans.append(end-start+1)
                start=i+1
        
        return ans


        


        