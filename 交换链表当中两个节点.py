"""
给你一个链表以及两个权值v1和v2，交换链表中权值为v1和v2的这两个节点。保证链表中节点权值各不相同，如果没有找到对应节点，那么什么也不用做。

 注意事项

你需要交换两个节点而不是改变节点的权值

您在真实的面试中是否遇到过这个题？ Yes
样例
给出链表 1->2->3->4->null ，以及 v1 = 2 ， v2 = 4
返回结果 1->4->3->2->null。"""
"""
首先需要交换的两个结点有可能是相邻的两个结点，而且有可能v1在v2后面，也有可能首结点就需要交换，那么我们还是一如既往的先设一个dummy结点，后面连上首结点，我们的思路是遍历整个链表，如果cur的下一个结点存在，且等于v1或v2中的一个，此时如果p1为空，说明这是要交换的第一个结点，我们将p1指向这个结点，然后讲pre指向cur，交换操作需要记录要交换的结点的前一个位置，然后继续遍历，当又遇到一个和v1或v2相等的结点，此时我们就需要交换了，我们用p2指向这个结点，然后用临时变量t指向下一个结点，此时我们需要判断cur和p1是相等，相等的话说明p1和p2是相邻的，我们只需要把p2移到p1前面去，如果不相等，说明p1和p2之间还有元素，那么我们交换p1和p2的位置即可，最后返回dummy->next即可："""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy
        f1, f2 = None, None
        while cur and cur.next:
            if cur.next.val == v1 or cur.next.val == v2:
                if not f1:
                    f1 = cur.next
                    pre = cur
                else:
                    temp = cur.next.next
                    f2 = cur.next
                    pre.next = f2
                    
                    if cur == f1:
                        f2.next = f1
                        f1.next = temp
                    else:
                        f2.next = f1.next
                        cur.next = f1
                        f1.next = temp
            cur = cur.next
        return dummy.next
