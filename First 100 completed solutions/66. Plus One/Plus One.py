class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_sent=""
        for num in digits:
            num_sent+=str(num)
        numb=str(int(num_sent)+1)
        return [int(x) for x in numb]


        
        