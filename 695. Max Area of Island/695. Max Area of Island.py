class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direc=[(0,1),(0,-1),(-1,0),(1,0)]
        m, n, max_area = len(grid), len(grid[0]), 0

        def dfs(r,c):
            grid[r][c]=0
            area=1

            for dr, dc in direc:
                nr=r+dr
                nc=c+dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                
                if grid[nr][nc]==1:
                    area+=dfs(nr,nc)
            return area
        

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area=max(max_area,dfs(i,j))
        
        return max_area