# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def printList(self, cur):
        result = []
        
        if cur is None:
            return result
        result.extend(self.printList(cur.left))
        result.extend([cur.val])
        result.extend(self.printList(cur.right))
    
        return result
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        return self.printList(root)