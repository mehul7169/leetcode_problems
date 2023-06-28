# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findPath(root, target):
            if not root:
                return
            target -= root.val
            if not root.left and  not root.right:
                if target == 0:
                    return True
                else:
                    return False
            return findPath(root.left, target) or findPath(root.right, target)

        return findPath(root, targetSum)