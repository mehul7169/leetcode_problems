class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def createSubtree(left, right):
            nonlocal index
            if left > right:
                return None
            root = TreeNode(preorder[index])
            index+=1

            root.left = createSubtree(left, inorder.index(root.val) - 1)
            root.right = createSubtree(inorder.index(root.val) + 1, right)

            return root
        
        index = 0
        
        return createSubtree(0, len(preorder) - 1)