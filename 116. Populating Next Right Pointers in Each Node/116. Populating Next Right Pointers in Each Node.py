"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q=deque([root])
        res=[]

        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j+1<len(res[i]):
                    res[i][j].next=res[i][j+1]
                else:
                    res[i][j].next=None
        return root



#solution 2
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q=deque([root])

        while q:
            n = len(q)
            for i in range(n):
                node=q.popleft()
                if i<n-1:
                    node.next=q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root




        