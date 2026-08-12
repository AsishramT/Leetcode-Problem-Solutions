class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pacific = set()
        atlantic = set()
        direc=[(0,1),(0,-1),(-1,0),(1,0)]

        def dfs(r,c,ocean):
            if (r,c) in ocean:
                return

            ocean.add((r,c))

            for dr,dc in direc:
                nr=r+dr
                nc=c+dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,ocean)
        
        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)
        
        for r in range(m):
            dfs(r,0,pacific)
            dfs(r,n-1,atlantic)

        
        return [list(loc) for loc in pacific if loc in atlantic]
        



