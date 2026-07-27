class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximumVal=0
        secondLargest=0

        for val in nums:
            if val >= maximumVal:
                secondLargest=maximumVal
                maximumVal=val
            elif val > secondLargest:
                secondLargest=val
        
        return (secondLargest-1) * (maximumVal-1)


        