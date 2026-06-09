class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes=0
        tempmaxOnes=0
        for value in nums:
            if value==1:
                tempmaxOnes+=1
                maxOnes=max(tempmaxOnes,maxOnes)
            else:
                tempmaxOnes=0
        return maxOnes

        