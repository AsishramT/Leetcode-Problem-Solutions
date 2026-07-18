from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small, big = float("inf") , 0

        for val in nums:
            if small > val:
                small=val
            if big < val:
                big=val

        for i in range(small,0,-1):
            if small % i == 0 and big % i == 0:
                return i




#a smaller version of the above code is as follows:
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums),min(nums))




        