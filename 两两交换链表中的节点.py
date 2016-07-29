"""


给一个链表，两两交换其中的节点，然后返回交换后的链表。
您在真实的面试中是否遇到过这个题？
样例

给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return None
        cur = head
        while cur and cur.next:
            temp = -1
            temp = cur.next.val
            cur.next.val = cur.val
            cur.val = temp
            cur = cur.next.next
        return head
            
