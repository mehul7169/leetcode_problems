class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        while root:
            return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)