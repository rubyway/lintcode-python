"""


有两个不同大小的二进制树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。
注意事项

若 T1 中存在从节点 n 开始的子树与 T2 相同，我们称 T2 是 T1 的子树。也就是说，如果在 T1 节点 n 处将树砍断，砍断的部分将与 T2 完全相同。
您在真实的面试中是否遇到过这个题？
样例

下面的例子中 T2 是 T1 的子树：

       1                3
      / \              / 
T1 = 2   3      T2 =  4
        /
       4

下面的例子中 T2 不是 T1 的子树：

       1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        temp = False
        if T2 is None:
            return True
        if T1 is None:
            return False
        if T1.val != T2.val:
            return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        elif T1.val == T2.val:
            temp = self.com(T1, T2)
            if temp:
                return True
            else:
                return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        return False
                
        
    def com(self, a, b):
        if (a is not None) and (b is not None) and (a.val == b.val):
                #if (a.left is not None) and (b.left is not None):
                return self.com(a.left, b.left) and self.com(a.right, b.right)  
                #if (a.right is not None) and (b.right is not None):
                    
        if (a is None) and (b is None):
            return True
        return False
            

