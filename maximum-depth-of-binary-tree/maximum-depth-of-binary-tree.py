# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countDepth(self, depth, root):
        maxValue = depth
        if root.left != None:
            maxValue = max(maxValue, self.countDepth(depth+1, root.left))
        if root.right != None:
            maxValue = max(maxValue, self.countDepth(depth+1, root.right))
            
        return maxValue
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        return self.countDepth(1, root)