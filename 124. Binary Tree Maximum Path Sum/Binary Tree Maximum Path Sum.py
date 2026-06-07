# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum=float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            L_S=max(dfs(node.left),0)
            R_S=max(dfs(node.right),0)

            self.maxSum=max(self.maxSum,L_S+R_S+node.val)
            return node.val+max(L_S,R_S)
            
        dfs(root)
        return self.maxSum
        