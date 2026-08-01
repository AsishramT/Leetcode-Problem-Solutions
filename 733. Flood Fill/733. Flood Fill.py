class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        start = image[sr][sc]

        if start == color:
            return image

        def dfs(r, c):
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == start:
                    dfs(nr, nc)

        dfs(sr, sc)
        return image