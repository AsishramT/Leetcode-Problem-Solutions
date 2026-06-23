# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([(root,0,0)])
        nodes=[]
        res=defaultdict(list)
        while q:
            for i in range(len(q)):
                node,row,col=q.popleft()
                nodes.append((col,row,node.val))
                if node.left:
                    q.append((node.left,row+1,col-1))
                if node.right:
                    q.append((node.right,row+1,col+1))
        nodes.sort()
        
        for col, row, value in nodes:
            res[col].append(value)

        return [res[col] for col in res.keys()]

#solution 2 (dfs)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        res=defaultdict(list)
        def dfs(node,row,col):
            if not node:
                return
            
            nodes.append((col,row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)

        dfs(root,0,0)
        nodes.sort()
        
        for col, row, value in nodes:
            res[col].append(value)

        return list(res.values())
        
        