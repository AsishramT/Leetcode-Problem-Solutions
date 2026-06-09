class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mNum=float('inf')

        while l<=r:
            mid=l+(r-l)//2
            if nums[r]<nums[mid]:
                l=mid+1
            else:
                r=mid-1
            mNum=min(nums[mid],mNum)
        return mNum
        