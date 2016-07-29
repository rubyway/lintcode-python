"""


给定一个排序链表，删除所有重复的元素每个元素只留下一个。
您在真实的面试中是否遇到过这个题？
样例

给出 1->1->2->null，返回 1->2->null

给出 1->1->2->3->3->null，返回 1->2->3->null
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
        if head is None:
            return None
        temp = ListNode(-1)
        temp.next = head
        pre = temp
        cur = head
        pos = head.next
        
        while pos:
            if cur.val == pos.val:
                pre.next = pos
                cur = pos
                pos = pos.next
            else:
                pre = cur
                cur = pos
                pos = pos.next
        return temp.next
                
