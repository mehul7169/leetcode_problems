# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def createSubtree(left, right):
            nonlocal index
            if left > right:
                return None
            root = TreeNode(postorder[index])
            index-=1

            root.right = createSubtree(inorder.index(root.val) + 1, right)
            root.left = createSubtree(left, inorder.index(root.val) - 1)
            

            return root
        
        index = len(postorder) - 1
        
        return createSubtree(0, len(postorder) - 1)