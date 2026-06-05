# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverter(node):
            if not node:
                return node

            node.left, node.right=node.right, node.left

            inverter(node.left)
            inverter(node.right)

            return node
        return inverter(root)
        