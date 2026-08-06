class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def backtracking(start):

            if start==len(s):
                res.append(path[:])
                return
            
            for i in range(start,len(s)):
                if isPalindrome(start,i):
                    path.append(s[start:i+1])
                    backtracking(i+1)
                    path.pop()
        backtracking(0)
        
        return res