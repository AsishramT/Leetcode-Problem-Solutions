# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        testList=[]
        def dfs(node):
            if not node:
                return None
            testList.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        for i in range(len(testList)):
            if i+1<len(testList):
                root.right=testList[i+1]
                root.left=None
                root=root.right
            
        