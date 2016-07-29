"""


检查两棵二叉树是否等价。等价的意思是说，首先两棵二叉树必须拥有相同的结构，并且每个对应位置上的节点上的数都相等。
您在真实的面试中是否遇到过这个题？
样例

    1             1
   / \           / \
  2   2   and   2   2
 /             /
4             4

就是两棵等价的二叉树。

    1             1
   / \           / \
  2   3   and   2   3
 /               \
4                 4

就不是等价的。
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
    #def isIdentical(a, b):
        l, r = False, False
        if a is None and b is None:
            return True
        if (a is None and b is not None) or (b is None and a is not None):
            return False
        if a.val != b.val:
            return False
        if a.val == b.val:
            l = self.isIdentical(a.left, b.left)
            r = self.isIdentical(a.right, b.right)
                
        return l and r
