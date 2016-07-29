"""
二叉树的前序遍历

    描述
    笔记
    数据
    评测

给出一棵二叉树，返回其节点值的前序遍历。
您在真实的面试中是否遇到过这个题？
样例

给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3

 返回 [1,2,3].
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        stack = []
        result = []
        while root or stack:
            if not root:
                root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
        return result
            
