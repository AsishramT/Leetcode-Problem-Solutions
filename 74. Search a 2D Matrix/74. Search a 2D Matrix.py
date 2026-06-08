class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        
        while l<=r:
            mid=l+(r-l)//2
            save=0
            for n in matrix[mid]:
                if n==target:
                    return True
                save=n
            if save> target:
                r=mid-1
            elif save<target:
                l=mid+1
        return False
                    
                
        