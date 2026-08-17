class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i

        for j in range(n + 1):
            dp[m][j] = n - j
        
        def dfs(i,j):

            if dp[i][j] != float("inf"):
                return dp[i][j]

            if word1[i]==word2[j]:
                dp[i][j] = dfs(i+1,j+1)
        
            else:
                dp[i][j] = 1 + min(
                    dfs(i + 1, j),       # delete
                    dfs(i, j + 1),       # insert
                    dfs(i + 1, j + 1)    # replace
                )
            
            return dp[i][j]


        return dfs(0,0)
