class Solution:
    def myAtoi(self, s: str) -> int:
        INTMAX=2147483647
        INTMIN=-2147483648

        ans=""

        s=s.strip()
        if not s:
            return 0

        if s[0]=="-":
            sign=-1
            s=s[1:]
        elif s[0]=="+":
            sign=1
            s=s[1:]
        elif s[0].isdigit() :
            sign=1
            ans+=s[0]
            s=s[1:]
        else:
            return 0
        
        for item in s:
            if item.isdigit():
                ans+=item
            else:
                break
        if not ans:
            return 0
        
        ans=sign*int(ans)

        if ans>INTMAX:
            return INTMAX
        elif ans<INTMIN:
            return INTMIN

        return ans