"""


给一棵二叉树，找出从根节点到叶子节点的所有路径。
您在真实的面试中是否遇到过这个题？
样例

给出下面这棵二叉树：

   1
 /   \
2     3
 \
  5

所有根到叶子的路径为：

[
  "1->2->5",
  "1->3"
]

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
    #def binaryTreePaths(root):
        if root is None:
            return []
        result = []
        #stack.append(root)
        def dfs(root, stack):
            if root.left is None and root.right is None:
                result.append(stack)
            if root.left:
                dfs(root.left, stack + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, stack + '->' + str(root.right.val))
        dfs(root, str(root.val))
        return result

