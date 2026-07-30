class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, ISLcount = len(grid), len(grid[0]), 0
        direc=[(0,1),(0,-1),(-1,0),(1,0)]

        def dfs(r, c):
            grid[r][c]="0"

            for dr, dc in direc:
                nr=r+dr
                nc=c+dc
                
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                
                if grid[nr][nc] == "1":
                    dfs(nr,nc)


        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    ISLcount+=1
                    dfs(i,j)
        
        return ISLcount
    

    

                
                    

                


                    





        