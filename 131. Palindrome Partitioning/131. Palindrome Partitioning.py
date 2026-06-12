class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]


        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start):
            if start==len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    path.append(s[start:i+1])
                    backtrack(i + 1)
                    path.pop()
        
        backtrack(0)
        return res


        