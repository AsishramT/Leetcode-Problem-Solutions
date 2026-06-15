class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=[]

        def backtrack(Open,closed):
            if len(path)==2*n:
                res.append("".join(path))
                return
            
            if Open < n:
                path.append("(")
                backtrack(Open+1,closed)
                path.pop()
            
            if closed < Open:
                path.append(")")
                backtrack(Open,closed+1)
                path.pop()
            
        

        backtrack(0,0)

        return res
        
        