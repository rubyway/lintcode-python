"""
给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的距离。

样例
给出一棵如下的二叉树:

        1

     /     \ 

   2       3

          /    \

        4      5  

这个二叉树的最小深度为 2"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right)+ 1 #左为空， 叶节点在右
        if root.right == None:
            return self.minDepth(root.left)+ 1 #右为空， 叶节点在左
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
   """def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left) 
        right = self.minDepth(root.right)
        if left and right:
            return min(left, right) + 1
        return max(left, right) + 1 #只有左或者右子树，所以需要在非空的上面找叶子节点"""
