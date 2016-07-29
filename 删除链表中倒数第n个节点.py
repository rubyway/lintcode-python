"""
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。



 注意事项

链表中的节点个数大于等于n

您在真实的面试中是否遇到过这个题？ Yes
样例
给出链表1->2->3->4->5->null和 n = 2.

删除倒数第二个节点之后，这个链表将变成1->2->3->5->null."""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        temp = ListNode(-1)
        pre = ListNode(-2)
        slow, fast = head, head
        temp = pre
        pre.next = slow
        i = 0
        while i< n:
            fast = fast.next
            i += 1
        while fast:
            fast = fast.next
            slow = slow.next
            pre = pre.next
        pre.next = slow.next
        
        return temp.next
