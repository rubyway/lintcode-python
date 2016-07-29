"""


合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。
您在真实的面试中是否遇到过这个题？
样例

给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        half = k>>1
        left, right = self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:])
        head = ListNode(0)
        cursor = head
        
        while left or right:
            if right == None or (left and left.val<= right.val):
                cursor.next = left
                left = left.next
            else:
                cursor.next = right
                right = right.next
            cursor = cursor.next
        return head.next    
