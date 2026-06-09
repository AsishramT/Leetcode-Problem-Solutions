# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_D=self.maxDepth(root.left)
        R_R_D=self.maxDepth(root.right)

        return max(left_D,R_R_D)+1
        