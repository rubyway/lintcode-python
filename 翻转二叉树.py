"""
翻转一棵二叉树


样例
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        while root == None:
            return None
        root.left, root.right = root.right, root.left
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        return root
