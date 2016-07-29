"""
回文链表

设计一种方式检查一个链表是否为回文链表。

样例
1->2->1 就是一个回文链表。"""
#http://bookshadow.com/weblog/2015/07/10/leetcode-palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        if head is None:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l, last = slow.next, None
        while l:
            temp = l.next
            l.next = last
            last, l = l, temp
        i, j = last, head
        while i and i.val == j.val:
            i, j = i.next, j.next
        return i is None
        
            

        
"""class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        templist = []
        while head:
            templist.append(head.val)
            head = head.next
        length = len(templist)
        i = 0
        while i < length/2:
            if templist[i] != templist[length- i- 1]:
                return False
        return True"""
            
