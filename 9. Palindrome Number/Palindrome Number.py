class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x=x
        self.x=str(self.x)
        palindX=self.x[::-1]
        
        if self.x==palindX:
            return True
        else:
            return False