class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        maximum=0
        for value in costs:
            if coins>=value:
                coins-=value
                maximum+=1
            else:
                break
        return maximum


#solution 2
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts=[0]*(max(costs)+1)

        for value in costs:
            counts[value]+=1


        maximum=0
    
        for cost,freq in enumerate(counts):
            if cost==0:
                continue
            
            could_buy=min(freq,coins//cost)

            maximum+=could_buy
            coins-=cost*could_buy

            if coins<cost:
                break
        return maximum
        


        