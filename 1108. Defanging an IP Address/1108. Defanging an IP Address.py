class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_str=""
        for ch in address:
            if ch==".":
                new_str= new_str +"[.]"
            else:
                new_str= new_str+ch
        return new_str