class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                
                if i == m - 1 and j == n - 1:
                    continue
                
                
                down = dp[i + 1][j] if i + 1 < m else 0
                right = dp[i][j + 1] if j + 1 < n else 0

                dp[i][j] = down + right
        return dp[0][0]