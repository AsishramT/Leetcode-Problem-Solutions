class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrS = sorted(arr)
        rank={}

        i=0
        for value in arrS:
            if value in rank:
                continue
            rank[value]=i+1
            i+=1
        
        return [rank[value] for value in arr]

        

#solution 2
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}

        for i, value in enumerate(sorted(set(arr)),1):
            rank[value]=i
        
        return [rank[value] for value in arr]

        

        