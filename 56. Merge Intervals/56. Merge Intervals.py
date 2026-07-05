class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res=[]

        choiceInt=intervals[0]

        for i in range(1,len(intervals)):
            currentInt=intervals[i]

            if currentInt[0]<=choiceInt[1]:
                choiceInt[1]=max(currentInt[1],choiceInt[1])
            else:
                res.append([choiceInt[0],choiceInt[1]])
                choiceInt=currentInt
        res.append([choiceInt[0],choiceInt[1]])
        return res




        