"""
给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）

给出一棵二叉树：
       1
      / \
     2   3
返回 6
"""
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
    def maxPathSum(self, root):
        self.result = None
        
        
        def subtreepathsum(node):
            if node is None:
                return 0
            left = subtreepathsum(node.left)#left为node左子树为顶点的子树和最大，所以返回值行只能是l+v,r+v,v三种情况，不能包含l+r+v
            right = subtreepathsum(node.right)
            self.result = max(max(0, left) + max(0, right) + node.val, self.result)#包含该节点的最大和，l+v,r+v,l+r+v,v
            return max(left, right, 0)+ node.val
            #返回值包含该节点的最大和
        subtreepathsum(root)
        return self.result
        
        
        
        
