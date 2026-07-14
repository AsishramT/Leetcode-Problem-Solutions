class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]

        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        while top <= bottom and left <= right:
            #going left to right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            if top > bottom: break
            
            #going top to bottom right side
            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1
            if left > right: break

            #going from right to left
            for k in range(right,left-1,-1):
                res.append(matrix[bottom][k])
            bottom-=1
            if top > bottom: break

            #going from bottom to top
            for l in range(bottom,top-1,-1):
                res.append(matrix[l][left])
            left+=1
            if left > right: break

        return res



        