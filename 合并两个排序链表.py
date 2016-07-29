"""
将两个排序链表合并为一个新的排序链表

您在真实的面试中是否遇到过这个题？ Yes
样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):

        temp = ListNode(-1)
        cur = ListNode(-2)
        temp.next = cur
        while l1 or l2:
            if l1 is None:
                cur.next = l2
                return temp.next.next
            if l2 is None:
                cur.next = l1
                return temp.next.next
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        return temp.next
