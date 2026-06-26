class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        while len(num)>1:
            after_num=0
            for digit in num:
                after_num+=int(digit)
            num=str(after_num)
        return int(num) 


        