"""


给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。
您在真实的面试中是否遇到过这个题？
样例

给出 1->2->3->3->4->4->5->null，返回 1->2->5->null

给出 1->1->1->2->3->null，返回 2->3->null
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        temp = ListNode(0)
        temp.next = head
        if head is None:
            return None
        if head.next is None:
            return head
        pre, cur, pos = temp, head, head.next
        check = -1
        while pos:
            if check != cur.val:
                if cur.val == pos.val:
                    check = cur.val
                    pre.next = pos
                    cur = pos
                    pos = pos.next
                else:
                    check = cur.val
                    pre = cur
                    cur = pos
                    pos = pos.next

            else:
                check = cur.val
                pre.next = pos
                cur = pos
                pos = pos.next  
                if (not pos) and check == cur.val:
                    pre.next = pos
        return temp.next
            
