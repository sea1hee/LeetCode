# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        while queue:
            cur = queue.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                queue.append(cur.left)
                queue.append(cur.right)
        
        return root