"""
从上往下打印二叉树

从上往下打印出二叉树的每个节点，同层节点从左至右打印。"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        queue = []
        result = []
        if root == None:
            return []
        queue.append(root)
        while queue != []: 
            temp = queue[0]
            queue = queue[1:]
            result.append(temp.val)
            if temp.left != None:
            	queue.append(temp.left)
                
            if temp.right != None:
            	queue.append(temp.right)

                
        return result
