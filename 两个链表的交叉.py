# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        lengtha, lengthb = 0, 0
        a = headA
        b = headB
        while a:
            a = a.next
            lengtha += 1
            
        while b:
            b = b.next
            lengthb += 1
        a = headA
        b = headB            
        temp = abs(lengtha- lengthb)
        while temp > 0:
            if lengtha > lengthb:
                a = a.next
            else:
                b = b.next
            temp -= 1
        while a and b:
            if a.val == b.val:
                return a
            a = a.next
            b = b.next
"""        tempa, tempb = headA, headB
        while tempa:
            tempb = headB
            while tempb:
                if tempa.val != tempb.val:
                    tempb = tempb.next
                else:
                    return tempb
            tempa = tempa.next
        return None"""

