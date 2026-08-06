class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
#now a O(1) space solution is possible by using two pointers to reverse the words in place but due to python string immutability we cannot do that in python. It is possible in C++ or other languages with mutable strings.