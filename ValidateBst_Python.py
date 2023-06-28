# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        def inorder(root):
            nonlocal output
            if not root:
                return
            inorder(root.left) 
            output.append(root.val)
            inorder(root.right)
        inorder(root)
        print(output)
        for i in range(len(output) - 1):
            if output[i + 1] <= output[i]:
                return False 

        return True
            
         