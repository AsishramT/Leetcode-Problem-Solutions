class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        min_cost=0
        taken=0
        for i in range(len(cost)-1,-1,-1):
            if taken==2:
                taken=0
            else:
                min_cost+=cost[i]
                taken+=1
        return min_cost



        