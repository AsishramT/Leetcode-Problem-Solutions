class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        prev = nums[1] - nums[0]
        length = 2 if prev != 0 else 1

        for i in range(1,len(nums)-1):
            curr=nums[i+1]-nums[i]
            if (curr > 0 and prev <= 0) or (curr < 0 and prev >= 0):
                length+=1
                prev=curr
            
        return length






        