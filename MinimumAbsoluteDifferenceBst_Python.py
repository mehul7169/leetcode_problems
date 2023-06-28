# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def getMin(nums):
            min = 10**6
            for i in range(len(nums) - 1):
                if nums[i+1] - nums[i] < min: min = nums[i+1] - nums[i]

            return min
        res = []
        def inorder(root):
            if root.left: inorder(root.left)
            res.append(root.val)
            if root.right: inorder(root.right)

        inorder(root)




        return getMin(res)