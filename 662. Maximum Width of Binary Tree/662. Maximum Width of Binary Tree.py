# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([(root,0)])
        max_width=0
        while q:
            lv_size=len(q)
            lv_start=q[0][1]
            level_end = q[-1][1]
            max_width = max(max_width, level_end - lv_start + 1)

            for i in range(len(q)):
                node, position = q.popleft()
                if node.left:
                    q.append((node.left, position * 2))
                if node.right:
                    q.append((node.right, position * 2 + 1))
                    
        return max_width


        