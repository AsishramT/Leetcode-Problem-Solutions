class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        used=set()

        def backtrack():
            if len(path)==len(nums):
                res.append(path[:])
                return
            
            for choice in nums:
                if choice not in used:
                    #adds the choice
                    path.append(choice)
                    used.add(choice)

                    #looks into other options
                    backtrack()

                    #removes last choice
                    path.pop()
                    used.discard(choice)

        backtrack()
        return res