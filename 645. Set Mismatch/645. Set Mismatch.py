class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashset=set()
        dup=None
        missed=None

        for value in nums:
            if value in hashset:
                dup=value
            hashset.add(value)
        
        for i in range(1,len(nums)+1):
            if i not in hashset:
                missed=i
                break



        return [dup,missed]
                

        