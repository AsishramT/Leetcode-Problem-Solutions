class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        the_num=0
        for item in nums:
            the_num^=item
        return the_num


        