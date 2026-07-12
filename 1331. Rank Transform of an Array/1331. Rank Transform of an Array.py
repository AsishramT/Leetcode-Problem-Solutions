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

        

        