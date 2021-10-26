# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        stack = []
        def travel(cur):
            if cur is None:
                return
        
            travel(cur.left)
            stack.append(cur.val)
            travel(cur.right)
        
        travel(root)
        
        stack.sort()
        return stack[k-1]
        
        
        