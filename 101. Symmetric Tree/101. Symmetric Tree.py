# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque([root])
        
        while q:
            level=[]
            n=len(q)

            for _ in range(n):
                node=q.popleft()
                
                if node:
                    level.append(node.val if node else None)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
                
            if level!=level[::-1]:
                return False
        return True



        