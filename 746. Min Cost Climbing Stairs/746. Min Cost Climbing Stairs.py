class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        m=len(cost)-1

        for i in range(len(cost)-1,-1,-1):
            right1=dp[i+1] if i+1 <= m else 0
            right2=dp[i+2] if i+2 <= m else 0
            
            dp[i]=cost[i]+min(right1,right2)
        return min(dp[0],dp[1])
