class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        maps = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def backtracking(ind,cur_comb):
            if ind == len(digits):
                res.append(cur_comb)
                return
            digit=digits[ind]
            letters=maps[digit]
            for letter in letters:
                backtracking(ind+1,cur_comb+letter)
        
        backtracking(0,"")
        return res