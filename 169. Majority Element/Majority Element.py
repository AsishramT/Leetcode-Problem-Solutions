class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count=0
        n=len(nums)//2
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        if nums.count(candidate)>n:
            return candidate