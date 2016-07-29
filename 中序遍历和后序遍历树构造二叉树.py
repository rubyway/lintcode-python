"""


根据中序遍历和后序遍历树构造二叉树
注意事项

你可以假设树中不存在相同数值的节点
您在真实的面试中是否遇到过这个题？
样例

给出树的中序遍历： [1,2,3] 和后序遍历： [1,3,2]

返回如下的树：

  2

 /  \

1    3
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
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if inorder== []:
            return None
        if postorder:
            root = postorder.pop()
        head = TreeNode(root)
        left = inorder[:inorder.index(root)]
        right = inorder[inorder.index(root)+ 1:]
        leftpos = postorder[:len(left)]
        rightpos = postorder[len(left):]
        
        head.left = self.buildTree(left, leftpos)
        head.right = self.buildTree(right, rightpos)
        return head
