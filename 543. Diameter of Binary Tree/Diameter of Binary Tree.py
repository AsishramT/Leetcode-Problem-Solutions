# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def maxH(node):
            if not node:
                return 0
            
            L_H=maxH(node.left)
            R_H=maxH(node.right)
            self.diameter = max(self.diameter, L_H + R_H)

            return max(L_H,R_H)+1
        maxH(root)
        return self.diameter

        