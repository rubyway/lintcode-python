# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        #tempsum = (l1.val + l2.val + tempjinwei)%10
        #tempjinwei = (l1.val + l2.val + tempjinwei)/10
        tempnode = ListNode(2)
        l = tempnode
        #python赋值和引用
        #上式是引用，针对的是同一个对象
        tempjinwei = 0
        #l1, l2 = l1.next, l2.next
        while l1 or l2 or tempjinwei:
            tempsum, tempjinwei = tempjinwei, 0
            if l1:
                tempsum += l1.val
                l1 = l1.next
            if l2:
                tempsum += l2.val
                l2 = l2.next            
            if tempsum >= 10:
                tempjinwei = 1
                tempsum -= 10
            l.next = ListNode(tempsum)
            l = l.next
        return tempnode.next


            
