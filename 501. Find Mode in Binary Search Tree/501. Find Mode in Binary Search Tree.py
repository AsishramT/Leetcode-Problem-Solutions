# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        count = 0
        max_count = 0
        modes = []

        def dfs(node):
            nonlocal prev, count, max_count, modes

            if not node:
                return
            
            dfs(node.left)

            if prev==node.val:
                count+=1
            else:
                count=1
            
            if count>max_count:
                max_count=count
                modes=[node.val]
            elif count == max_count:
                modes.append(node.val)
            
            prev=node.val

            dfs(node.right)

        dfs(root)
        return modes
        