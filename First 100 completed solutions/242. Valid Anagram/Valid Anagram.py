class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_c=Counter(s)
        t_c=Counter(t)

        for letter, freq in s_c.items():
            if freq != t_c[letter]:
                return False
        return True
        