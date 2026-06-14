# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        valueBook={}
        def dfs(node):
            if not node:
                return

            if node.val in valueBook:
                valueBook[node.val]+=1
            else:
                valueBook[node.val]=1

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
    
        for num in valueBook:
            remainder=k-num

            if remainder in valueBook:
                if remainder != num:
                    return True
                elif valueBook[remainder]>1:
                    return True
    
        return False
            

        