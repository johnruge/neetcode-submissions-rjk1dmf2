# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def addOne(node, currMax):
            nonlocal res
            if not node:
                return
            if node.val >= currMax:
                res += 1         

            currMax = max(currMax, node.val)
            
            addOne(node.left, currMax)
            addOne(node.right, currMax)
        
        res = 0
        addOne(root, float('-inf'))
        return res

# O(n) complexity 
# O(h) space complexity (recursion stacks)
        