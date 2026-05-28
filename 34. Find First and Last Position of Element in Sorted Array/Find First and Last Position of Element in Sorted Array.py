class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            firstind=nums.index(target)
            nums=sorted(nums,reverse=True)
            lastind=nums.index(target)
            return [firstind,len(nums)-lastind-1]
        else:
            return [-1,-1]