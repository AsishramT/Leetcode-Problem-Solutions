class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        movingI=0
        count=nums.count(0)
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[movingI] = nums[i]
                movingI+=1
        
        del nums[len(nums)-count: ]

        for i in range(count):
            nums.append(0)
        return nums
        
                
        