class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        path=[]

        def backtrack(start):
            res.append(path[:])
            for i in range(start,n):
                choice=nums[i]
                if i>start and nums[i] == nums[i - 1]:
                    continue
                path.append(choice)

                backtrack(i+1)

                path.pop()

        
        backtrack(0)
        return res

solution=Solution()
print(solution.subsetsWithDup([1,2,2]))