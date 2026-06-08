class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while l<=r:
            mid=(r+l)//2
            if int(mid)*int(mid)==num:
                return True
            elif int(mid)*int(mid)<num:
                l=mid+1
            else:
                r=mid-1
        return False
            
        