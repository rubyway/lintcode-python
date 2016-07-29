"""


找到单链表倒数第n个节点，保证链表中节点的最少数量为n。
您在真实的面试中是否遇到过这个题？
样例

给出链表 3->2->1->5->null和n = 2，返回倒数第二个节点的值1.

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
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if head is None:
            return None
        
        #tempnode = ListNode(-1)
        slow, fast = head, head
        
        i = 0
        while i< n:
            fast = fast.next
            i += 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
        
