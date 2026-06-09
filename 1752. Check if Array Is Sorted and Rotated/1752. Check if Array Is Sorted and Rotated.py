class Solution:
    def check(self, nums: List[int]) -> bool:
        prev=float("-inf")
        breaks=0
        for num in nums:
            if num>=prev:
                prev=num
                continue
            else:
                breaks+=1
                prev=num
        n=len(nums)
        if nums[n-1]>nums[0]:
            breaks+=1
        if breaks>1:
            return False

        return True





        