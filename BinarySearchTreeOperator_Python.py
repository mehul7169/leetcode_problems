# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [0]
        self.index = 0


        
        def inorder(root):
            if not root:
                return
            if not root.left and not root.right:
                self.stack.append(root.val)
                return

            inorder(root.left)
            self.stack.append(root.val)
            inorder(root.right)
        inorder(root)
        print(self.stack)

    def next(self) -> int:
        self.index += 1
        return self.stack[self.index]

    def hasNext(self) -> bool:
        if len(self.stack) > self.index + 1:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()