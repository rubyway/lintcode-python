"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None:
            return False
        if head.next is None:
            return False
        
        slow, fast = head, head.next
        
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow== fast:
                return True
        return False
            
