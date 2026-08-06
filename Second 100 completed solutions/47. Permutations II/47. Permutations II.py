class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        start=nums[:]
        all_perms=[]
        while True:
            all_perms.append(nums[:])

            n = len(nums)

            pivot = -1

            # Find pivot
            for i in range(n - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    pivot = i
                    break

            if pivot == -1:
                nums.reverse()
            else:
                for j in range(n-1,pivot,-1):
                    if nums[j]>nums[pivot]:
                        nums[j],nums[pivot]=nums[pivot],nums[j]
                        break
                
                left=pivot+1
                right=n-1
                while left<right:
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
                    right-=1
            if start==nums:
                break
        return all_perms
            
        