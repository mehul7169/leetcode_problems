# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        hashmap = {}
        index = 0

        def preorder(node):
            nonlocal index
            if not node:
                return
            hashmap[index] = node
            index += 1

            preorder(node.left)
            preorder(node.right)

        preorder(root)
        size = index
        index = 0
        for i in range(size - 1):
            node = hashmap[index]
            node.right =  hashmap[index + 1]
            node.left = None
            index += 1
        print(hashmap.keys())
        print(index)
        lastNode = hashmap[index]
        lastNode.right = lastNode.left = None