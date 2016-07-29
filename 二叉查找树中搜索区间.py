"""


给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。
您在真实的面试中是否遇到过这个题？
样例

如果有 k1 = 10 和 k2 = 22, 你的程序应该返回 [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12

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
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        if root is None:
            return []
        result = []
      
        def search(root, k1, k2):
            if root is None:
                return
            if root.val < k1:
                search(root.right, k1, k2)
            elif root.val > k2:
                search(root.left, k1, k2)
            elif root.val <= k2 and root.val >= k1:
                result.append(root.val)
                search(root.left, k1, k2)
                search(root.right, k1, k2)       
        search(root, k1, k2)
        return sorted(result)
