# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        cur = head
        st = [cur]
        while cur.next:
            cur = cur.next
            st.append(cur)
            
        head = st[-1]
        del st[-1]
        cur = head
        while st:
            cur.next = st[-1]
            del st[-1]
            cur = cur.next
        
        cur.next = None
        return head