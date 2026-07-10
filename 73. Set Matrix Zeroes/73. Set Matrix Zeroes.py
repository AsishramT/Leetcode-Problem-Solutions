class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        ZeroLoc=[]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    ZeroLoc.append((i,j))
        
        while ZeroLoc:
            upDown, LefRi = ZeroLoc.pop()
            up,down = upDown,upDown
            left,right = LefRi,LefRi
                
            while up - 1 >= 0 or down + 1 < m:
                if up - 1 >= 0 and matrix[up - 1][LefRi]:
                    matrix[up - 1][LefRi] = 0
                up -= 1

                if down + 1 < m and matrix[down + 1][LefRi]:
                    matrix[down + 1][LefRi] = 0
                down += 1
            
            while left - 1 >= 0 or right + 1 < n:
                if left - 1 >= 0 and matrix[upDown][left - 1]:
                    matrix[upDown][left - 1] = 0
                left -= 1

                if right + 1 < n and matrix[upDown][right + 1]:
                    matrix[upDown][right + 1] = 0
                right += 1
            
            



# second try optimized solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        cols=set()
        rows=set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    cols.add(j)
                    rows.add(i)
        
        for col in cols:
            i=0
            while i<m:
                matrix[i][col]=0
                i+=1

        for row in rows:
            j=0
            while j<n:
                matrix[row][j]=0
                j+=1
        


            
            



        