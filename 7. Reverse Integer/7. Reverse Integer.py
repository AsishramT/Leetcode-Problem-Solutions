class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2**31 -1
        INT_MIN = -(2**31)
        
        sign = 1 if x >= 0 else -1

        ans=int(str(abs(x))[::-1])*sign
        
        return ans if INT_MIN <= ans <= INT_MAX else 0
        




#soln 2 if we want to avoid storing numbers larger than 32 bit signed integer
class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2**31 -1
        INT_MIN = -(2**31)
        
        sign = 1 if x >= 0 else -1

        ans=str(abs(x))[::-1]
        
        return int(ans)*sign if INT_MIN <= int(ans)*sign <= INT_MAX else 0
#soln 3 if we want to avoid storing numbers larger than 32 bit signed integer and also avoid using string conversion
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return rev * sign
        




        