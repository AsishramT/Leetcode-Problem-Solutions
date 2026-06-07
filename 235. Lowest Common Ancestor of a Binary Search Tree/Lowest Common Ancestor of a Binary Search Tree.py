# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,n1,n2):
            if not node:
                return True
            
            if node.val>n1.val and node.val > n2.val:
                return dfs(node.left,n1,n2)
            
            if node.val<n1.val and node.val<n2.val:
                return dfs(node.right,n1,n2)
            
            return node

        return dfs(root,p,q)


        