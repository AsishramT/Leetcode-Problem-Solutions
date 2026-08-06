class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        digitprod=1

        while True:
            for value in str(n):
                digitprod *= int(value)
            if digitprod%t==0:
                return n
            else:
                digitprod=1
                n+=1

        