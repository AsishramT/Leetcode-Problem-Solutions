class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi,mx=min(nums),max(nums)
        st=set(nums)
        ans=[]

        for i in range(mi+1,mx):
            if i not in st:
                ans.append(i)
        return ans