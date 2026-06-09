class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        for i in range(n-1):
            curr=[]
            cnt=1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    cnt+=1
                else:
                    curr.append(str(cnt))
                    curr.append(s[i-1])
                    cnt=1
            curr.append(str(cnt))
            curr.append(s[-1])

            s = "".join(curr)
        return s

        
        

        


        