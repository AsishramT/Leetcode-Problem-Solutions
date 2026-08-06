class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        INT_MAX = 2**31 - 1

        if dividend == -2**31 and divisor == -1:
            return INT_MAX
        
        neg= (dividend<0) != (divisor<0)
        
        q=0
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        while dvd >= dvs:
            temp = dvs
            mult = 1
            while dvd>=(temp << 1):
                temp <<=1
                mult <<=1
            dvd-=temp
            q+=mult
            

        if neg:
            q=-q
        
        return q
            
            
        