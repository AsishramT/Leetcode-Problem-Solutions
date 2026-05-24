class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Mapper={}

        for i in range(len(nums)):
            Mapper[nums[i]]=i
        for i in range(len(nums)):
            NeededAmt= target-nums[i]
            if NeededAmt in Mapper and Mapper[NeededAmt] !=i:
                return[i,Mapper[NeededAmt]]
        return []
        


