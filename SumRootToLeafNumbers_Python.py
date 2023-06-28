# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        def sumSub(root, s):
            if not root:
                return
            s += str(root.val)
            if not root.left and not root.right:
                result.append(int(s))
            
            sumSub(root.left, s)
            sumSub(root.right, s)
        
        sumSub(root, '')

        return sum(result)