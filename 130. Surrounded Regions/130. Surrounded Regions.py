class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        direc=[(0,1),(0,-1),(-1,0),(1,0)]
        safe=set()

        def dfs(r,c):
            if (r,c) in safe or board[r][c] != "O":
                return
            
            safe.add((r,c))

            for dr,dc in direc:
                nr=r+dr
                nc=c+dc

                if not(0<=nr<m and 0<=nc<n):
                    continue
                dfs(nr,nc)
        
        for r in range(m):
            dfs(r,0)
            dfs(r,n-1)
        
        for c in range(n):
            dfs(0,c)
            dfs(m-1,c)
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in safe:
                    board[r][c]="X"

        


        