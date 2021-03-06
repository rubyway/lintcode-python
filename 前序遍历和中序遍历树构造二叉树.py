"""


根据前序遍历和中序遍历树构造二叉树.
注意事项

你可以假设树中不存在相同数值的节点
您在真实的面试中是否遇到过这个题？
样例

给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:

  2
 / \
1   3

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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if inorder== []:
            return None
        if preorder:
            root = preorder[0]
            preorder = preorder[1:]
            
        head = TreeNode(root)
        left = inorder[:inorder.index(root)]
        right = inorder[inorder.index(root)+ 1:]
        leftpre = preorder[:len(left)]
        rightpre = preorder[len(left):]
        
        head.left = self.buildTree(leftpre, left)
        head.right = self.buildTree(rightpre, right)
        return head
