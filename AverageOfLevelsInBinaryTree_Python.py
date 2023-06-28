# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = [root]
        output = []
        def getAverage(queue):
            return sum([x.val for x in queue]) / len(queue)
        while queue:
            output.append(getAverage(queue))
            curr_level = queue
            queue = []
            while curr_level:
                curr = curr_level.pop(0)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                
            print([x.val for x in queue])
        return output

        