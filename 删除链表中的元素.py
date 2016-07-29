"""
删除链表中的元素

 描述
 笔记
 数据
 评测
删除链表中等于给定值val的所有节点。

样例
给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        temp = ListNode(0)#哨兵节点
        temp.next = head#位于头的前一节点
        prenode = temp#等号表示引用，即同时指向同一个节点对象
        nownode = head
        while nownode:
            if nownode.val == val:
                prenode.next = nownode.next#遇到相同节点值，跳过去，并且前后连接
            else:
                prenode = nownode#遇到不同的，不做处理，前后连接
            nownode = nownode.next#遍历
                  
        return temp.next#nownode由于遍历指向后边的节点了，但是temp指向的节点没变
