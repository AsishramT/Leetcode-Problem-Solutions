class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=[]
        right_sum=[]
        ans=[]
        for i in range(len(nums)):
            LS=sum(nums[0:i])
            RS=sum(nums[i+1:])
            left_sum.append(LS)
            right_sum.append(RS)
        for i in range(len(nums)):
            ans.append(abs(left_sum[i]-right_sum[i]))

        return ans

#solution 2
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n

        totS = sum(nums)
        LS = 0

        for i in range(n):
            RS = totS - LS - nums[i]
            ans[i] = abs(LS - RS)
            LS += nums[i]

        return ans


        