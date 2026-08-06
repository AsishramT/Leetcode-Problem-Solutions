# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]

        def dfs(rt):
            if not rt:
                return
            dfs(rt.right)
            self.stack.append(rt.val)
            dfs(rt.left)

        dfs(root)


    def next(self) -> int:
        return self.stack.pop()
        

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#best solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]

        self.pushl(root)

    def pushl(self,node):
        while node:
            self.stack.append(node)
            node=node.left

    def next(self) -> int:
        node=self.stack.pop()
        self.pushl(node.right)
        return node.val
        

    def hasNext(self) -> bool:
        return len(self.stack)>0      


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()