
from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)

        res=high

        while low<=high:
            mid =(low+high)//2
            summed=0

            for n in nums:
                summed+=ceil(n/mid)

            if summed<=threshold:
                res=mid
                high=mid-1
            else:
                low=mid+1
                
            
        return res



        