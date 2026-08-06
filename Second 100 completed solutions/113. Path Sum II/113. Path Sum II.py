# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path=[]
        res=[]
        def dfs(node, remaining):
            if not node:
                return
            
            path.append(node.val)
            
            if not node.left and not node.right and remaining==node.val:
                res.append(path[:])
            
            leftS=dfs(node.left,remaining-node.val)
            rightS=dfs(node.right,remaining-node.val)

            path.pop()

        dfs(root,targetSum)
        return res
        
            


        




        

        